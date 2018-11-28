#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

double currentCookies;
double cpersec;
double time;

double cookieClick(double C,double F,double X)
{
   bool buyFarm=true;
   time=0.;
   currentCookies=0.;
   cpersec=2.;
   double timeneed ;

  while(buyFarm)
  {
    timeneed=(X-C)/cpersec;

    buyFarm=false;
   //   printf ("%d ",time);
     if(timeneed > X/(cpersec+F))
     {
       time+=C/cpersec;
       buyFarm=true;
       currentCookies=0;
       cpersec+=F;
     }


    }//end of while

    time+=X/cpersec;

return time;
}


int main()
{
 FILE *f;
 FILE *g;

 int tests;
 f=fopen("cookie.txt","w");
 g=fopen("cookie.in.txt","r");
  fscanf(g,"%d",&tests);
 double X,F,C;


for (int i=1;i<=tests;i++)
{
  fscanf (g,"%lf %lf %lf",&C,&F,&X);
  fprintf(f,"Case #%d: %.7f\n",i,cookieClick(C,F,X));
}

fclose(f);
fclose(g);
return 0;
}
