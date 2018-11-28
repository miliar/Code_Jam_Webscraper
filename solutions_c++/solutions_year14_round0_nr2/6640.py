#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

double C,F,X;
int main() {
  int T;
  scanf("%d", &T);

  for(int t=1;t<=T; t++) {
    scanf("%lf %lf %lf", &C, &F, &X);

    double rate = 2;

    // time for one cookie
    double best = X*(1.0/rate);

    bool better = true;
    double mytime = 0;
    while(better) {
      mytime += C*(1.0/rate);
      rate +=F;
      double res = mytime + X*(1.0/rate);

      if (res < best) {
        best = res;
      } else {
      better = false;
      }
    }

    printf("Case #%d: %.7lf\n", t, best);
    
  }
}
