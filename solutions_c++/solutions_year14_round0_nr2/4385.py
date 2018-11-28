#include <stdio.h>

int main() {
  double c, f, x;
  int T;
  scanf("%d", &T);
  for (int cnt = 1; T--; ++cnt) {
    scanf("%lf %lf %lf", &c, &f, &x);
    double spd = 2, time_sum = 0, time_y, time_n;
    while (x > c) {
      time_sum += c / spd;
      time_y = x / (spd + f);
      time_n = (x - c) / spd;
      if (time_y <= time_n) {
        spd += f;
      } else {
        x -= c;
        break;
      }
    }
    time_sum += x / spd;
    printf("Case #%d: %0.7lf\n", cnt, time_sum);
  }
  return 0;
}
