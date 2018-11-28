/* Written by Filip Hlasek 2016 */
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

int R, C;

int go[2][4] =  { {1, 0, 3, 2}, {3, 2, 1, 0} };

char ans;

#define MAXN 1111
int nb[MAXN];
char m[MAXN][MAXN];
int startx[MAXN], starty[MAXN], startstate[MAXN];

bool ok(int i) {
  int x = startx[i], y = starty[i], state = startstate[i];
  /*
  REP(r, R) {
    m[r][C] = '\0';
    printf("%s\n", m[r]);
  }
  printf("i: %d x: %d y: %d state: %d\n", i, x, y, state);
  */
  while (true) {
    // printf("x: %d y: %d state: %d\n", x, y, state);
    if (x < 0 || x == R || y < 0 || y == C) REP(j, 2 * (R + C)) {
      int nx = min(max(0, x), R - 1), ny = min(max(0, y), C - 1), ns = (state + 2) % 4;
      // printf("nx: %d ny: %d ns: %d j: %d x: %d y: %d s: %d\n", nx, ny, ns, j, startx[j], starty[j], startstate[j]);
      if (j != i && nx == startx[j] && ny == starty[j] && ns == startstate[j]) {
        return j == nb[i];
      }
    }
    if (state == 0 && m[x][y] == '\\') { y++; state = 3; }
    else if (state == 1 && m[x][y] == '\\') { x--; state = 2; }
    else if (state == 2 && m[x][y] == '\\') { y--; state = 1; }
    else if (state == 3 && m[x][y] == '\\') { x++; state = 0; }

    else if (state == 0 && m[x][y] == '/') { y--; state = 1; }
    else if (state == 1 && m[x][y] == '/') { x++; state = 0; }
    else if (state == 2 && m[x][y] == '/') { y++; state = 3; }
    else if (state == 3 && m[x][y] == '/') { x--; state = 2; }
  }
}

bool ok() {
  REP(i, 2 * (R + C)) if (!ok(i)) return false;
  return true;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(testcase, 1, T) {
    scanf("%d%d", &R, &C);
    REP(i, (R + C)) {
      int a, b;
      scanf("%d%d", &a, &b); a--; b--;
      nb[a] = b;
      nb[b] = a;
    }
    REP(i, C) { startx[i] = 0; starty[i] = i; startstate[i] = 0; }
    REP(i, R) { startx[i + C] = i; starty[i + C] = C - 1; startstate[i + C] = 1; }
    REP(i, C) { startx[i + R + C] = R - 1; starty[i + R + C] = C - 1 - i; startstate[i + R + C] = 2; }
    REP(i, R) { startx[i + C + C + R] = R - 1 - i; starty[i + C + C + R] = 0; startstate[i + C + C + R] = 3; }

    printf("Case #%d:\n", testcase);
    int S = R * C;
    bool fine = false;
    REP(mask, 1 << S) {
      REP(i, R) REP(j, C) {
        if (mask & (1 << (C * i + j))) m[i][j] = '\\';
        else m[i][j] = '/';
      }
      if (ok()) {
        REP(i, R) {
          m[i][C] = '\0';
          printf("%s\n", m[i]);
        }
        fine = true;
        break;
      }
    }
    if (!fine) printf("IMPOSSIBLE\n");
  }
  return 0;
}
