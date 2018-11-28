#include <bits/stdc++.h>
using namespace std;
int r[100];
int c[100];
int main() {
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    int n;
    double vv, xx, rr, cc;
    int v, x, sum = 0;
    int maxx = 0, minn = 999999999;
    scanf("%d %lf %lf", &n, &vv, &xx);
    v = round(vv * 10000);
    x = round(xx * 10000);
    for (int i = 0; i < n; i++) {
      scanf("%lf %lf", &rr, &cc);
      r[i] = round(rr * 10000);
      c[i] = round(cc * 10000);
      maxx = max(c[i], maxx);
      minn = min(c[i], minn);
      sum += r[i];
    }
    if (maxx < x || minn > x) {
      printf("Case #%d: IMPOSSIBLE\n", tt);
      continue;
    }
    long long d = 1LL * v * x;
    if (maxx == minn) {
      printf("Case #%d: %.8lf\n", tt, 1.0 * v / sum);
      continue;
    }
    double a = (d - 1.0 * c[1] * v) / (c[0] - c[1]);
    printf("Case #%d: %.8lf\n", tt, max(a / r[0], (v - a) / r[1]));
  }
  return 0;
}

