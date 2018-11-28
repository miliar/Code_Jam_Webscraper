#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

double f[101][101], a[201], c[201];
int test, n, m;

int main() {
     freopen("b.in", "r", stdin);
     freopen("b.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          scanf("%d%d", &n, &m);
          for (int i = 1; i <= n; ++i) scanf("%lf", &a[i]);
          sort(a + 1, a + n + 1);
          double ans = 0;
          for (int i = 0; i <= m; i++) {
               int len = 0;
               for (int j = 1; j <= i; j++) c[++len] = a[j];
               for (int j = n - (m - i) + 1; j <= n; j++) c[++len] = a[j];
               memset(f, 0, sizeof(f));
               f[0][0] = 1;
               for (int k = 1; k <= len; k++)
                    for (int l = 0; l < k && l <= len / 2; l++)
                         if (k - 1 - l <= len / 2) {
                              int x = k - 1 - l;
                              if (l < len / 2) f[l + 1][x] += f[l][x] * c[k];
                              if (x < len / 2) f[l][x + 1] += f[l][x] * (1.0 - c[k]);
                         }
               ans = max(ans, f[len / 2][len / 2]);
          }
          printf("Case #%d: %.10f\n", uu, ans);
     }
}
