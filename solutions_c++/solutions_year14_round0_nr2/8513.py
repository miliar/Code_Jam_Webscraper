#include <cstdio>

int main() {
  int T; scanf(" %d", &T);
  for (int t = 1; t <= T; t++) {
    double c, f, x; scanf(" %lf %lf %lf", &c, &f, &x);
    double ans = x/2.0, time_sum = 0.0; int n = 0;
    while (ans > time_sum+(c/(2+n*f))+(x/(2+(n+1)*f))) {
      time_sum += c/(2+n*f); n++;
      ans = time_sum+(x/(2+n*f));
    }
    printf("Case #%d: %.7lf\n", t, ans);
  }
}
