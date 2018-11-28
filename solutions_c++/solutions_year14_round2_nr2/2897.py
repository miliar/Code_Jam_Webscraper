#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
   int T;
   freopen("B-small-attempt0.in","r",stdin);
   freopen("ayaya.out","w",stdout);
   scanf("%d",&T);
   for(int a=0;a<T;a++){
      int A,B,K, win, temp;
      win =0;
      scanf("%d",&A);
      scanf("%d",&B);
      scanf("%d",&K);
      for(int i=0;i<A;i++){
         for(int j=0;j<B;j++){
            temp = i&j;
            if(temp<K) win+=1;
         }
      }
      printf("Case #%d: %d\n",a+1,win);
   }
   return 0;
}
