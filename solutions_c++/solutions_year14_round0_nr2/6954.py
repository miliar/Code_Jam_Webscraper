
#include <stdlib.h>
#include <stdio.h>


int main(void)
{
   double C[1000],F[1000]={0},X[1000],time,K=2,time1,time2,f1,f2;
   int i,T;
   scanf("%d",&T);
   for(i=1;i<=T;i++)
   {
      scanf("%lf",&C[i]);
       scanf("%lf",&F[i]);
	scanf("%lf",&X[i]);
   }
for(i=1;i<=T;i++)
{
time=0;
time2=0;
time1=0;
K=2;
f1=0;f2=0;
   time=C[i]/2;

   f1=2+F[i];
   f2=2;
   time1=(X[i])/f1;
   time2=(X[i]-C[i])/f2;
   while(time1<time2)
   {
   		K=K+F[i];
   		
   time=time+(C[i]/K);
   
   	
   		f1=K+F[i];
   		f2=K;
      time1=(X[i])/f1;
   time2=(X[i]-C[i])/f2;
   }
   time=time+time2;
   /* clean up */
   printf("\nCase #%d: %f",i,time);
}
   return 0;
}
