#include <cstdio>

int main(){
  int T;
  scanf("%d",&T);
  for(int t=1; t<=T; ++t){
    // C = farm price, F = farm cps, X = target
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);
    double cps = 2;
    double bestTime = X/cps;
    double time = 0;
    while(true){
      time += C/cps;
      cps = cps + F;
      if( (time+X/cps) > bestTime )
        break;
      bestTime = time+X/cps;
    }
    
    printf("Case #%d: %.7f\n",t,bestTime);
  }
}
