/* Opgave: A */
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
#include <cstdint>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;

char field[100][100];

void doit(int testcase) {
  int R, C;
  cin >> R >> C;
  for (int r = 0; r < R; ++r)
    for (int c = 0; c < C; ++c)
      cin >> field[r][c];
  bool possible = true;
  int cnt = 0;
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      if (field[r][c] == '.')
        continue;
      bool downAllowed = false;
      bool upAllowed = false;
      bool leftAllowed = false;
      bool rightAllowed = false;

      for (int r2 = 0; r2 < r; ++r2)
        if (field[r2][c] != '.')
          upAllowed = true;
      for (int r2 = r + 1; r2 < R; ++r2)
        if (field[r2][c] != '.')
          downAllowed = true;
      for (int c2 = 0; c2 < c; ++c2)
        if (field[r][c2] != '.')
          leftAllowed = true;
      for (int c2 = c + 1; c2 < C; ++c2)
        if (field[r][c2] != '.')
          rightAllowed = true;
      if (!downAllowed && !upAllowed && !leftAllowed && !rightAllowed)
        possible = false;
      if((field[r][c] == '^' && !upAllowed) || (field[r][c] == 'v' && !downAllowed) || (field[r][c] == '<' && !leftAllowed) || (field[r][c] == '>' && !rightAllowed))
        ++cnt;
    }
  }
  cout << "Case #" << testcase << ": ";
  if(!possible)
    cout << "IMPOSSIBLE";
  else
    cout << cnt;
  cout << "\n";
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
    doit(i);
  return 0;
}
/* Opgave: A */
