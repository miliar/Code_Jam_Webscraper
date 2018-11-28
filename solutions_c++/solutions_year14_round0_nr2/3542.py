#include <stdio.h>
int main()
{
    int t,i,j,k;
    double c,f,x,rate,time,ans;
    double farm[100005];
    scanf("%d",&t);
    for (k = 1; k <= t; k++) {
          rate = 2.0;
          time  = 0; 
          scanf("%lf%lf%lf",&c,&f,&x);
          for (i = 0; i < 100005; i++) {
              farm[i] = time + (double)x/rate;
              time = time + (double)c/rate;
              rate = rate + f;
              
              if (i == 0)
                 continue;
              if (farm[i] >= farm[i-1]) {
                 ans = farm[i-1];
                 break;
              }
          }
         // printf("hello\n");
        /*  for (j = 0; j <= i; j++) {
              printf("%.7lf ",farm[j]);
          }
          printf("\n");
          */
          printf("Case #%d: %.7lf\n",k,ans);
    }
    return 0;
}
              
              
          
