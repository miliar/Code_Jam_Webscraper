#include <iostream>
using namespace std;

const int dr[4] = {-1,1,0,0};
const int dc[4] = {0,0,1,-1};
string dirs = "^v><";
char grid[111][111];
int R, C;

int go(int _r, int _c) {
  int md = dirs.find(grid[_r][_c]);
  if (md == -1) {
    return 0;
  }

  bool ok = false;
  for (int i = 0; i < 4; i++) {
    unsigned r = _r, c = _c;
    r += dr[i];
    c += dc[i];
    while (r < R && c < C) {
      if (grid[r][c] != '.') {
        ok = true;
        if (i == md) {
          return 0;
        }
      }
      r += dr[i];
      c += dc[i];
    }
  }

  if (ok) return 1;
  return 1e9;
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
      cin >> grid[i];
    }
    int ans = 0;
    for (int i = 0; i < R && ans < 1e5; i++)
      for (int j = 0; j < C && ans < 1e5; j++)
        ans += go(i, j);

    if (ans > 100000) {
      printf("Case #%d: IMPOSSIBLE\n", t);
      continue;
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
