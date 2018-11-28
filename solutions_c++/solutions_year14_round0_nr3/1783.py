/* Written by Filip Hlasek 2014 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

int _R, _C;
#define MAXN 111
bool m[MAXN][MAXN], visited[MAXN][MAXN];

int nb(int x, int y) {
  int ans = 0;
  FOR(dx, -1, 1) FOR(dy, -1, 1) {
    int nx = x + dx, ny = y + dy;
    if (nx < 0 || ny < 0 || nx >= _R || ny >= _C) continue;
    ans += m[nx][ny];
  }
  return ans;
}

void print(int x, int y) {
  REP(i, _R) {
    REP(j, _C) {
      if (i == x && j == y) printf("c");
      else if (m[i][j]) printf("*");
      else printf(".");
    }
    printf("\n");
  }
}

void dfs(int x, int y) {
  visited[x][y] = true;
  if (nb(x, y) == 0) {
    FOR(dx, -1, 1) FOR(dy, -1, 1) {
      int nx = x + dx, ny = y + dy;
      if (nx < 0 || ny < 0 || nx >= _R || ny >= _C) continue;
      if (!m[nx][ny] && !visited[nx][ny]) dfs(nx, ny);
    }
  }
}

void solve(int R, int C, int M) {
  _R = R; _C = C;
  REP(mask, 1 << (R * C)) {
    int mines = 0;
    REP(i, R) REP(j, C) {
      if (mask & (1 << (C * i + j))) {
        m[i][j] = true;
        mines++;
      }
      else m[i][j] = false;
    }
    if (mines != M) continue;
    REP(i, R) REP(j, C) {
      if (nb(i, j) == 0 || (!m[i][j] && M == R * C - 1)) {
        REP(ii, R) REP(jj, C) visited[ii][jj] = false;
        dfs(i, j);
        bool ok = true;
        REP(ii, R) REP(jj, C) if(!m[ii][jj] && !visited[ii][jj]) ok = false;
        if (ok) { print(i, j); return; }
      }
    }
  }
  printf("Impossible\n");
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  REP(t, T) {
    int R, C, M;
    scanf("%d%d%d", &R, &C, &M);
    printf("Case #%d:\n", t + 1);
    solve(R, C, M);
  }
  
  return 0;
}
