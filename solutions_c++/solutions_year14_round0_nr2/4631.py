#include <stdio.h>
#include <algorithm>
using namespace std;

double c, f, x;
double inc;

int main () {
  int teste;
  scanf ("%d", &teste);
  for (int t = 0; t < teste; t++) {
    scanf ("%lf %lf %lf\n", &c, &f, &x);
    inc = 2.0;
    double ret = 0;
    while (x/inc > x/(inc + f) + c/inc) {
      ret += c/inc;
      inc += f;
    }
    ret += x/inc;
    printf ("Case #%d: %.7lf\n", t + 1, ret);
  }
  return 0;
}
