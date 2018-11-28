#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, n, m;
char str[111][111];

bool work(int x, int y, int dx, int dy) {
     x += dx; y += dy;
     for (; x >= 1 && y >= 1 && x <= n && y <= m; x += dx, y += dy)
          if (str[x][y] == '.') continue;
          else return true;
     return false;
}
 
int main() {
     freopen("a.in", "r", stdin);
     freopen("a.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          printf("Case #%d: ", uu);
          scanf("%d%d", &n, &m);
          for (int i = 1; i <= n; i++) scanf("%s", str[i] + 1);
          bool ans = true; int value = 0;
          for (int i = 1; i <= n && ans; i++) 
               for (int j = 1; j <= m && ans; j++) {
                    if (str[i][j] == '.') continue;
                    if (str[i][j] == '<') {
                         if (work(i, j, 0, -1)) continue;
                         if (work(i, j, 0, 1) || work(i, j, 1, 0) || work(i, j, -1, 0)) ++value;
                         else ans = false;
                    }
                    if (str[i][j] == '>') {
                         if (work(i, j, 0, 1)) continue;
                         if (work(i, j, 0, -1) || work(i, j, 1, 0) || work(i, j, -1, 0)) ++value;
                         else ans = false;
                    }
                    if (str[i][j] == '^') {
                         if (work(i, j, -1, 0)) continue;
                         if (work(i, j, 0, -1) || work(i, j, 0, 1) || work(i, j, 1, 0)) ++value;
                         else ans = false;
                    }
                    if (str[i][j] == 'v') {
                         if (work(i, j, 1, 0)) continue;
                         if (work(i, j, 0, -1) || work(i, j, 0, 1) || work(i, j, -1, 0)) ++value;
                         else ans = false;
                    }
               }
          if (!ans) printf("IMPOSSIBLE\n");
          else printf("%d\n", value);
     }
}
