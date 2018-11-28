#include <bits/stdc++.h>
using namespace std;

const double eps = 1e-8;
double r[10], c[10], x, v;

int main() {
  int test; scanf("%d", &test);
  for (int cas = 1; cas <= test; ++cas) {
    int n; int a, b, cc, d;
    scanf("%d%d.%d%d.%d", &n, &a, &b, &cc, &d);
    v = a * 10000 + b;
    x = cc * 10000 + d;
    if (n == 1) {
      scanf("%d.%d%d.%d", &a, &b, &cc, &d);
      r[0] = a * 10000 + b;
      c[0] = cc * 10000 + d;
      if (c[0] == x) {
        printf("Case #%d: %.9f\n", cas, v / r[0]);
      } else {
        //printf("%d %.4f %.4f\n", n, v, x);
        //printf("%.4f %.4f\n", r[0], c[0]);
        printf("Case #%d: IMPOSSIBLE\n", cas);
      }
    } else {
      for (int i = 0; i < 2; ++i) {
        scanf("%d.%d%d.%d", &a, &b, &cc, &d);
        r[i] = a * 10000 + b;
        c[i] = cc * 10000 + d;
      }
      if (c[0] > c[1]) {
        swap(r[0], r[1]);
        swap(c[0], c[1]);
      }
      if (x < c[0] || x > c[1]) {
        //printf("%d %.4f %.4f\n", n, v, x);
        //printf("%.4f %.4f\n", r[0], c[0]);
        //printf("%.4f %.4f\n", r[1], c[1]);
        printf("Case #%d: IMPOSSIBLE\n", cas);
      } else if (c[0] == c[1]) {
        printf("Case #%d: %.9f\n", cas, v / (r[0] + r[1]));
      } else {
        double k = (x - c[0]) / (c[1] - c[0]);
        double aa = v * (1 - k) / r[0], bb = v * k / r[1];
        printf("Case #%d: %.9f\n", cas, aa > bb ? aa : bb);
      }
    }
  }
  return 0;
}
