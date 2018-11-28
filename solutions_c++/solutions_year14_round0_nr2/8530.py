#include<stdio.h>

int main()
{
  int t;
  double c,f,x;
	scanf("%d",&t);
   for(int i=0;i<t;i++){
	   scanf("%lf %lf %lf",&c,&f,&x);
	   double previousCostIfNotTaken = 0;
	   double currentCostIfNotTaken = 0;
	   double totalCostifTaken = 0 ;
	   double rateOfCookie = 2;
	   previousCostIfNotTaken = x/rateOfCookie;
	   //printf("preivcost %lf\n",previousCostIfNotTaken);
	   while(true){
		   /*if(previousCostIfNotTaken < currentCostIfNotTaken){
			   break;
		   }*/
		   totalCostifTaken += c/rateOfCookie;
		   //printf("total %lf\n",totalCostifTaken);
		   rateOfCookie = rateOfCookie + f;
		   //printf("rate %d\n",rateOfCookie);
		   currentCostIfNotTaken = totalCostifTaken + (x/rateOfCookie);
		   //printf("curent cost %lf\n",currentCostIfNotTaken);
		   if(previousCostIfNotTaken < currentCostIfNotTaken){
			  // printf("in if");
			   	   	   break;
		   		   }
		   previousCostIfNotTaken = currentCostIfNotTaken;
	   }
	   //printf("-----");
	   printf("Case #%d: %.7lf\n",i+1,previousCostIfNotTaken);
   }

 return 0;
}

