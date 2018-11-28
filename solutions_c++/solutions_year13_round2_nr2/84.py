#include <stdio.h>
#include <cmath>
#include <memory.h>

long double f[3333][3333];

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
//  printf("%lf\n", log(c[300][150])/log(10));
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    int cur = 1;
    while (n > cur) {
      n -= cur;
      cur += 4;
    }
    int ax = (x < 0 ? -x : x);
    double ans;
    if ((ax + y) / 2 > (cur-1) / 4) ans = 0.0; else
    if ((ax + y) / 2 < (cur-1) / 4) ans = 1.0; else {
      if (x == 0) {
        if (n == cur) ans = 1.0;
        else ans = 0.0;
      } else
      if (n == cur) ans = 1.0; else
      {
        int up = (cur - 1) / 2;
        memset(f, 0, sizeof(f));
        f[0][0] = 1;
        for (int i=0;i<=up;i++)
          for (int j=0;j<=up && i+j<n;j++) {
            if (i == up) {
              f[i][j+1] += f[i][j];
            } else
            if (j == up) {
              f[i+1][j] += f[i][j];
            } else {
              f[i+1][j] += 0.5*f[i][j];
              f[i][j+1] += 0.5*f[i][j];
            }
          }
        ans = 0.0;
        for (int i=y+1;i<=up;i++)
          if (n-i <= up) ans += f[i][n-i];
      }
    }
    printf("%.17lf\n", ans);
  }
  return 0;
}
