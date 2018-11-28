#include <stdio.h>

int main(){

  int T;
  scanf("%d", &T);

  for(int k = 1; k<=T; k++){
    
    double C,X, F;
    scanf("%lf %lf %lf", &C, &F, &X);
    double t = 0;
    double Prod = 2;
    while(  X/(Prod) - X/(Prod+F) > C/Prod){
      //printf("%lf\n", t);
      t += C/Prod;
      Prod += F;
    }
    //printf("%lf\n", t);
    t += X/Prod;

    printf("Case #%d: %lf\n", k, t);
  }

  return 0;
}
