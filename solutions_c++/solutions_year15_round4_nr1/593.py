/* Written by Filip Hlasek 2015 */
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

#define MAXN 111
int N, M;
char m[MAXN][MAXN];

int D[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

void solve_testcase() {
  scanf("%d%d", &N, &M);
  REP(i, N) scanf("%s", m[i]);
  int ans = 0;
  REP(i, N) REP(j, M) if (m[i][j] != '.') {
    int dd;
    switch (m[i][j]) {
      case '^': dd = 0; break;
      case '>': dd = 1; break;
      case 'v': dd = 2; break;
      case '<': dd = 3; break;
    }
    bool ok = false, ok2 = false;
    REP(d, 4) {
      int dx = D[d][0], dy = D[d][1];
      int x = i + dx, y = j + dy;
      while (x >= 0 && y >= 0 && x < N && y < M) {
        if (m[x][y] != '.') {
          if (d == dd) ok = true;
          ok2 = true;
          break;
        }
        x += dx; y += dy;
      }
    }
    if (!ok) {
      if (!ok2) { printf("IMPOSSIBLE\n"); return; }
      ans++;
    }
  }
  printf("%d\n", ans);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    solve_testcase();
  }
  return 0;
}
