#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 110;

char a[MAX][MAX];
int dx[] = {0, +1, 0, -1};
int dy[] = {+1, 0, -1, 0};

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int n, m;
    scanf("%d %d", &n, &m);
    REP(i, n) scanf("%s", a[i]);
    
    int ans = 0;
    REP(i, n) REP(j, m) {
      if (a[i][j] == '.') continue;

      int k;
      if (a[i][j] == '>') k = 0; else
        if (a[i][j] == 'v') k = 1; else
          if (a[i][j] == '<') k = 2; else
            if (a[i][j] == '^') k = 3; else
              assert(false);

      int c[4];
      REP(l, 4) c[l] = 0;
      REP(l, 4) {
        int x = i + dx[l], y = j + dy[l];
        while (0 <= x && x < n && 0 <= y && y < m) {
          if (a[x][y] != '.') { c[l] = 1; break; }
          x += dx[l], y += dy[l];
        }
      }

      if (c[k]) continue;
      if (accumulate(c, c + 4, 0) == 0) { ans = -1; break; }
      ans++;
    }

    printf("Case #%d: ", tp);
    if (ans == -1) puts("IMPOSSIBLE"); else
      printf("%d\n", ans);
  }
  return 0;
}
