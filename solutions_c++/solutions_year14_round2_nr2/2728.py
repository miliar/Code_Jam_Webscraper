#include <stdio.h>

int main(){
   int T, A, B, K;
   int C;
   int count;
   
   //freopen("Lottery.in","r",stdin);
   //freopen("Lottery.out","w",stdout);
   
   scanf("%d",&T);
   for (int i = 0; i < T; i++){
      scanf("%d",&A);
      scanf("%d",&B);
      scanf("%d",&K);
      count = 0;
      for (int j = 0; j < A; j++){
         for (int k = 0; k < B; k++){
            C = j & k;
            //printf("C = %d vs K = %d\n",C,K);
            if (C < K) count++;
         }
      }
      printf("Case #%d: %d\n",i+1,count);
   }
   return 0;
}
