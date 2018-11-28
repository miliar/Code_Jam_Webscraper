#include <bits/stdc++.h>
using namespace std;
char m[105][105];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
bool ok[105][105];
int r, c, ans;
char opp[5] = "v<^>";
bool dfs(int x, int y) {
  ok[x][y] = true;
  int d;
  if (m[x][y] == '^') d = 0;
  if (m[x][y] == '>') d = 1;
  if (m[x][y] == 'v') d = 2;
  if (m[x][y] == '<') d = 3;
  while (true) {
    x += dx[d];
    y += dy[d];
    if (x <= 0 || x > r || y <= 0 || y > c) return false;
    if (m[x][y] != '.') {
      if (ok[x][y]) return true;
      bool o = dfs(x, y);
      if (!o) {
        m[x][y] = opp[d];
        ans++;
      }
      return true;
    }
  }
}
bool solve() {
  scanf("%d %d", &r, &c);
  for (int i = 1; i <= r; i++) {
    scanf("%s", m[i] + 1);
  }
  int dir;
  ans = 0;
  for (int i = 1; i <= r; i++) {
    for (int j = 1; j <= c; j++) {
      if (m[i][j] != '.') {
        bool o = dfs(i, j);
        if (!o) {
          ans++;
          int k = 0;
          for (; k < 4; k++) {
            m[i][j] = opp[k];
            if (dfs(i, j)) break;
          }
          if (k == 4) {
            return false;
          }
        }
      }
    }
  }
  return true;
}
int main() {
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    if (solve()) {
      printf("Case #%d: %d\n", tt, ans);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", tt);
    }
  }
  return 0;
}

