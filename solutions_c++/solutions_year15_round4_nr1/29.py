/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

const int N = 100;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
const char *str = "><v^";
int w, h;
char s[N][N + 1];

bool check( int x, int y, int k ) {
  for (x += dx[k], y += dy[k]; 0 <= x && x < w && 0 <= y && y < h; x += dx[k], y += dy[k])
    if (s[y][x] != '.')
      return 1;
  return 0;

}

void solve() {
  scanf("%d%d ",&h, &w);
  forn(i, h)
    gets(s[i]);
  int res = 0;
  forn(i, h)
    forn(j, w)
      if (s[i][j] != '.') {
        int dir = strchr(str, s[i][j]) - str;
        if (!check(j, i, dir)) {
          res++;
          int good = 0;
          forn(k, 4) 
            if (check(j, i, k))
              good++;
          if (!good) {
            puts("IMPOSSIBLE");
            return;
          }            
        }
      }
  printf("%d\n", res);
}

int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
