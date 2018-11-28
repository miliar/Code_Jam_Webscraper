#include<iostream>
using namespace std;
double getTimeForCookieTarget(double farmCost,double increment, double cTarget, double cGenRate)
{
       double curTargetTime=cTarget/cGenRate;
       if (curTargetTime < (farmCost/cGenRate + cTarget/(cGenRate+increment)))
       {
          return (curTargetTime);
       }
       else
       {    
          return ( farmCost/cGenRate +getTimeForCookieTarget(farmCost,increment,cTarget,cGenRate+increment));         
       }
}
int main ()
{
    double time,increment,farmCost,cTarget,cGenRate=2;
    int testCases;
    scanf("%d",&testCases);
    for (int tCase = 1; tCase <= testCases; tCase++)
    {
       scanf("%lf %lf %lf", &farmCost, &increment, &cTarget);
       time=getTimeForCookieTarget(farmCost,increment,cTarget,cGenRate);
       printf ("Case #%d: %.7f\n",tCase,time);    
    }
    return(0);
}
