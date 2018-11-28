#include <stdio.h>

int main(){
  
  int t, T, i, j;
  double C, F, X, ans, y, z;

  scanf("%d", &T);
  for(t=1; t<=T; t++){
    scanf("%lf %lf %lf", &C, &F, &X);
    ans = X/2.0;
    i=1;
    y=0;
    while(1){
      y+=C/(2.0 + F*(i-1));
      z = y + X/(2.0 + F*i);
      if(z < ans) ans = z;
      else break;
      i++;
    }
    printf("Case #%d: %.7lf\n", t, ans);
  }

  
  return 0;
}
