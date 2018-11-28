#include <cstdio>
#include <cassert>
#include <cstring>
#include <cmath>

/*
 * C/2 + C/(2+F) + ... + X/(2+nF)
 *
 * X/(2+nF) <= X/(2+(n+1)F) + C/(2+nF)
 * X*(2+nF+F) <= X*(2+nF) + C*(2+nF+F)
 * X*F <= C*(2+(n+1)*F)
 * (F*(X-C)-2C)/(F*C) <= n ----- too sensible
 */

int main (void) {
  int T;
  scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    double C;
    double F;
    double X;
    scanf("%lf", &C);
    scanf("%lf", &F);
    scanf("%lf", &X);
    /*int n = (int) ceil((F*(X-C)-2*C)/(F*C));
    if (n < 0) n = 0;*/ // TOO sensible
    double sum = 0;
    int n;
    for (n = 0; X * F > C * (2+(n+1)*F); n++) {
      sum += C / (2+n*F);
    }
    sum += X / (2+n*F);
    printf("Case #%d: %.7lf\n", currentcase, sum);
  }
  return 0;
}
