#include <cstdio>
#include <cstdlib>
#include <algorithm>

double C,F;

double min;

double solve(double rate , double X , double current)
{
  double ratio = 0.0, rest, next_rest;
  double next_ratio;
  while(1){
    rest = X / rate;
    next_ratio = ratio + (C/rate);
    rate += F;
    next_rest = X / rate;
   // printf("%f %f\n",ratio+rest, next_ratio + next_rest);
    if( ((rest + ratio) - (next_ratio + next_rest)) < 10e-8){
      return ratio + rest;
    }
    ratio = next_ratio;
    rest  = next_rest;
  }
}

int main( int argc, char * argv[] )
{
  int T,i;
  double X;
  scanf("%d",&T);
  for( i = 1; i <= T; i++ ){  
    scanf( "%lf%lf%lf", &C, &F, &X );
    min = X;
    printf( "Case #%d: %.7f\n",i,solve(2.0,X,0.0));
  }
  return 0;
}
