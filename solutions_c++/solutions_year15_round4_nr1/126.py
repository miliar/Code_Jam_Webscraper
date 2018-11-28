#include <cassert>
#include <cstring>

#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAXN = 123;

int r, s;
char grid[MAXN][MAXN];

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};
const string DIRS = "^>v<";

bool valid(int x, int y) {
  if (x < 0 || y < 0) return false;
  if (x >= r || y >= s) return false;
  return true;
}

bool is_ok(int x, int y, int d) {
  x += dx[d], y += dy[d];
  while (valid(x, y)) {
    if (grid[x][y] != '.') return true;
    x += dx[d], y += dy[d];
  }
  return false;
}

int main(void) {
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    scanf("%d %d", &r, &s);
    REP(i, r) scanf("%s", grid[i]);

    int cnt = 0;
    bool ok = true;
    REP(i, r) REP(j, s) {
      int c = DIRS.find(grid[i][j]);
      if (c != -1) {
        if (is_ok(i, j, c)) continue;
        // inace
        int d; for (d = 0; d < 4; ++d) if (is_ok(i, j, d)) { ++cnt; break; }
        if (d == 4) ok = false;
      }
    }

    printf("Case #%d: ", tc+1);
    if (!ok) puts("impossible");
    else printf("%d\n", cnt);
    fflush(stdout);
  }
  return 0;
}   
