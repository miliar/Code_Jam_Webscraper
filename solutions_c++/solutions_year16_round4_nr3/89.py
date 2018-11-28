#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, n, m, a[101][101], t[101][101], f[1001], w[1001][4], p[1001];

int gf(int i) {
     if (i == f[i]) return f[i];
     return f[i] = gf(f[i]);
}

int go(int x, int y, int d) {
     if (!x || x == n + 1 || !y || y == m + 1) {
          return a[x][y];
     }
     if (t[x][y] == 0)
          if (d == 0) return go(x, y - 1, 3);
          else if (d == 1) return go(x - 1, y, 2);
          else if (d == 2) return go(x, y + 1, 1);
               else return go(x + 1, y, 0);
     else
          if (d == 0) return go(x, y + 1, 1);
          else if (d == 1) return go(x + 1, y, 0);
          else if (d == 2) return go(x, y - 1, 3);
               else return go(x - 1, y, 2);
}
     
     
bool soso(int x, int y, int cnt, int len) {
     if (x == n + 1) {
          for (int i = 1; i <= (n + m) << 1; i += 2)
               if (p[i] <= m) { 
                    if (go(1, p[i], 0) != p[i + 1]) return false;
               }
               else if (p[i] <= n + m) { 
                    if (go(p[i] - m, m, 3) != p[i + 1]) return false;
               } 
               else if (p[i] <= n + m * 2) { 
                    if (go(n, m - (p[i] - n - m) + 1, 2) != p[i + 1]) return false;
               } else
               if (go(n - (p[i] - n - m - m) + 1, 1, 1) != p[i + 1]) return false;
          for (int i = 1; i <= n; i++) {
               for (int j = 1; j <= m; j++) if (!t[i][j]) printf("/");
               else printf("\\");
               printf("\n");
          }
          return true;
     }
     int nx = x, ny = y + 1;
     if (ny == m + 1) ny = 1, nx++;
     t[x][y] = 0;
     if (soso(nx, ny, cnt + 2, len)) return true;
     t[x][y] = 1;
     if (soso(nx, ny, cnt + 2, len)) return true;
     return false;
}

int main() {
     freopen("c.in", "r", stdin);
     freopen("c.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          printf("Case #%d:\n", uu);
          scanf("%d%d", &n, &m);
          for (int i = 1; i <= (n + m) << 1; i++) scanf("%d", &p[i]);
          int cnt = 0;
          for (int i = 1; i <= m; i++) a[0][i] = ++cnt;
          for (int i = 1; i <= n; i++) a[i][m + 1] = ++cnt;
          for (int i = m; i; i--) a[n + 1][i] = ++cnt;
          for (int i = n; i; i--) a[i][0] = ++cnt;
          for (int i = 1; i <= n; i++)
               for (int j = 1; j <= m; j++) a[i][j] = ++cnt;
          if (!soso(1, 1, 1, cnt)) printf("IMPOSSIBLE\n");
     }
}
     
