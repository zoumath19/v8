# Copyright 2016 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

print("""
1
v8-foozzie source: name/to/a/file.js
2
v8-foozzie source: name/to/file.js
  weird other error
^
3
unknown
""")

if '--bad-flag' in sys.argv:
  print('bad behavior')
if '--very-bad-flag' in sys.argv:
  print('very bad behavior')
if '--jitless' in sys.argv:
  print('jitless flag passed')
