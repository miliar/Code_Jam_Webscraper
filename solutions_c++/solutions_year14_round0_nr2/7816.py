#include <iostream>
#include <stdio.h>
using namespace std;

int main ()
{
  int t;
  double rl, ll, c, f, x, p, time;
  int h = 1;
  scanf ("%d", &t);
  while (h <= t) {
    scanf ("%lf %lf %lf", &c, &f, &x);
    p = 2.0;
    time = 0.0;
    rl = f * x;
    ll = c * f;
    rl = rl - ll;
    while (c * p < rl) {
      time = time + (c / p);
      p = p + f;
    }

    time = time + x / p;

    printf ("Case #%d: %.7lf\n", h++, time);
  }

  return 0;
}
