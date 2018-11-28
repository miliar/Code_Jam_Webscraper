#include <bits/stdc++.h>
using namespace std;

int r, c;
char mp[110][110];
const int dx[] = { 0, 1, 0,-1};
const int dy[] = { 1, 0,-1, 0};
char dir[] = ">v<^";

int solve() {
  int cc = 0;
  for (int i = 0; i < r; ++i)
    for (int j = 0; j < c; ++j) {
      if (mp[i][j] == '.') continue;
      int delta = 1; bool flag = false;
      for (int k = 0; k < 4; ++k) {
        int x = i, y = j;
        do {
          x += dx[k]; y += dy[k];
        } while (0 <= x && x < r && 0 <= y && y < c && mp[x][y] == '.');
        if (0 <= x && x < r && 0 <= y && y < c) {
          flag = true;
          if (mp[i][j] == dir[k])
            delta = 0;
        }
      }
      if (!flag) return -1;
      cc += delta;
    }
  return cc;
}

int main() {
  int test; scanf("%d", &test);
  for (int cas = 1; cas <= test; ++cas) {
    scanf("%d%d", &r, &c);
    for (int i = 0; i < r; ++i)
      scanf("%s", mp[i]);
    int ans = solve();
    if (ans == -1) {
      printf("Case #%d: IMPOSSIBLE\n", cas);
    } else {
      printf("Case #%d: %d\n", cas, ans);
    }
  }
  return 0;
}
