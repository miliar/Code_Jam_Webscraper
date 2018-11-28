#include <cstdio>

int main() {
  int t;
  double c, f, x, y, r;
  scanf("%d", &t);
  for (int cn = 1; cn <= t; cn++) {
    scanf("%lf %lf %lf", &c, &f, &x);
    y = 0;
    r = 2;
    while (x / r > (c / r) + x / (r + f)) {
      y += c / r;
      r += f;
    }
    y += x / r;
    printf("Case #%d: %.7lf\n", cn, y);
  }
  return 0;
}
