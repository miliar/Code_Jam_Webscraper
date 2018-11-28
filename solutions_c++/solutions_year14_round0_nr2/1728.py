#include <stdio.h>
#include <string.h>

double c, f, x;

int main() {
  int t;
  scanf("%d", &t);
  for (int cases = 1; cases <= t; ++ cases) {
    scanf("%lf %lf %lf", &c, &f, &x);

    double time = 0, rate = 2;

    printf("Case #%d: ", cases);
    if (c >= x) { printf("%.7lf\n", x / rate); continue; }


    while (true) {
      time += c / rate;
      if ( x / (rate + f) < (x - c) / rate ) rate += f;
      else { time += (x - c) / rate; break; }
    }

    printf("%.7lf\n", time);
  }
  return 0;
}
