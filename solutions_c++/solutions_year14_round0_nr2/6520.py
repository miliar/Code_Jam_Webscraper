#include <cstdio>

int main() {
  double c, x, f, t;
  int n;
  //freopen("/Users/lx/POJ/B-large.in", "r", stdin);
  //freopen("/Users/lx/POJ/B-large.out", "w", stdout);
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) {
    scanf("%lf %lf %lf", &c, &f, &x);
    t = 0;
    int k = (int)((f*x-2*c)/(c*f));
    for (int j = 0; j < k; ++j)
      t += c/(2.0+j*f);
    if (k < 0)
      k = 0;
    t += x/(2.0+k*f);
    printf("Case #%d: %.7lf\n", i, t);
  }
}