#include <cstdio>

const double eps = 1e-10;

int main() {
  int t;
  double C,F,X;
  double y, opt, sum;
  int max;
  scanf("%d", &t);
  for ( int tc = 1; tc <= t; tc++ ){
    scanf("%lf%lf%lf", &C, &F, &X);
    opt = X/2.0;
    max = X+1;
    y = 0;
    
    for ( int i = 0; i <= max; i++) {
      y += ( C/(2+i*F) );
      sum = y + X/(2+ (i+1)*F );
      if ( opt-sum > eps )
        opt = sum;
    }
    printf("Case #%d: %.7f\n", tc, opt);
  }
  return 0;
}
