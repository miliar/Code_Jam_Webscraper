#include <stdio.h>

main() {

  int T;
  scanf("%d",&T);
  
  for (int t = 1; t <= T; t++) {

    long double ans = 0;
    long double C,F,X;

    scanf("%Lf %Lf %Lf",&C,&F,&X);

    int k = (int) ((X*F-2*C)/(C*F) - 0.000000001) ;
    
    if (k <0) k = 0;
    //    printf("%d %Lf, %Lf, %Lf\n", k,C,F,X);
    for (int i = 0; i < k; i++) {
      ans += C/(2+i*F);
    }
    ans += X/(k*F+2);
    

    

    printf("Case #%d: %.7Lf\n",t,ans);

  }
  


}
