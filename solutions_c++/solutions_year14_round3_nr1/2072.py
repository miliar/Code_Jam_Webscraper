#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
   int T;
   freopen("A-small-attempt4.in","r",stdin);
   freopen("1_small.out","w",stdout);
   scanf("%d",&T);
   long double rattable[41];
   for(int a=0;a<40;a++){
      rattable[a] = pow(2.0, -(a+1.0));
   }
   for(int a=0;a<T;a++){
      int P,Q;
      scanf("%d/%d",&P,&Q);
      double p,q,gen, gen2, ratio, ratio2,aya;
      p = P;
      q = Q;
      aya = log2(q);
      double roundaya= floor(aya);
      ratio = ratio2 = q/p;
      ratio = ceil(ratio);
      //printf("%f\n",ratio);
      gen = log2(ratio);
      gen2 = log2(ratio2);
      //printf("%f\n",ratio2);
      //printf("%f %f\n",gen,gen2);
      if((aya!=roundaya) && (gen!=gen2)){
         printf("Case #%d: impossible\n",a+1);
      }
      else{
         int jason =0;
         while(1){
            if((p/q)>=rattable[jason]) break;
            jason++;
         }
         //int b = gen;
         printf("Case #%d: %d\n",a+1,jason+1);
      }
   }
   return 0;
}
