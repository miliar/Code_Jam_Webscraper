#include<stdio.h>

int main()
{
  int testCases;
  double c,f,x;
  scanf("%d",&testCases);
   for(int i=0 ; i< testCases ; i++)
   {
	   scanf("%lf %lf %lf",&c,&f,&x);
	   double previousValueFarmNotBought = 0, currentValueFarmNotBought = 0,totalValueFarmBought = 0 ;
	   double currentRateOfCookieProduction = 2;
	   previousValueFarmNotBought = x/currentRateOfCookieProduction;
	   for(;;)
	   {
		   totalValueFarmBought = totalValueFarmBought + (c/currentRateOfCookieProduction);
		   currentRateOfCookieProduction = currentRateOfCookieProduction + f;
		   currentValueFarmNotBought = totalValueFarmBought + (x/currentRateOfCookieProduction);
		   if(previousValueFarmNotBought < currentValueFarmNotBought)
		   {
			   	   	   break;
		   }
		   previousValueFarmNotBought = currentValueFarmNotBought;
	   }
	   printf("Case #%d: %.7lf\n",i+1,previousValueFarmNotBought);
   }
 return 0;
}

