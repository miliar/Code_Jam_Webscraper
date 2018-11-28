#include <stdio.h>
#include <stdlib.h>
//c is the price
//f is the increment
//x is the goal
int main(){
   int T;
   double X,F,C;
   freopen("B-large.in","r",stdin);
   freopen("cookieLarge.out","w",stdout);
   scanf("%d",&T);
   for(int a=1;a<=T;a++){
      int rounds =0;
      double totalUpPrev =0;
      double totalUp =0;//total IF upgrade
      double totalFull=0;//total IF wait till X 
      double totalFullPrev=0;
      double upgrade=0;
      double rate =2;
      double full=0;
      scanf("%lf",&C);
      scanf("%lf",&F);
      scanf("%lf",&X);
      while(1){
         rounds++;
         upgrade=C/rate;
         full=X/rate;
         if(rounds==1){
            totalUpPrev+=upgrade;
            totalUp+=upgrade;
            totalFullPrev+=full;
            totalFull+=full;
            //printf("totalup= %.7lf\n",totalUp);
            //printf("totalupprev= %.7lf\n",totalUpPrev);
            //printf("totalFull= %.7lf\n",totalFull);
            //printf("totalFullprev= %.7lf\n",totalFullPrev);
            if(upgrade<full){
               rate+=F;
               continue;
            }
            else break;
         }
         else{
            totalUp+=upgrade;
            totalFull=totalUpPrev+full;
            //printf("totalup= %.7lf\n",totalUp);
            //printf("totalupprev= %.7lf\n",totalUpPrev);
            //printf("totalFull= %.7lf\n",totalFull);
            //printf("totalFullprev= %.7lf\n",totalFullPrev);
            if(totalFull>totalFullPrev){
               break;
            }
            else{
               totalUpPrev=totalUp;
               totalFullPrev=totalFull;
               rate+=F;
            }
         }
      }
      printf("Case #%d: %.7lf\n",a,totalFullPrev);
   }
}
