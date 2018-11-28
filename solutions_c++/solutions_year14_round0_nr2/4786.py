#include<stdio.h>

double leastTime(double x,double c,double curr,double f)
{

if((x/curr)<(c/curr)+(x/(curr+f)))
    return x/curr;

double a;
a=leastTime(x,c,curr+f,f);
if((x/curr)<(c/curr)+a){

   return x/curr;}
else{

    return ((c/curr)+a);}
}

int main()
{

int t;
scanf("%d",&t);
for(int l=1;l<=t;l++)
{
    double c,x,f,curr;
    scanf("%lf",&c);
    scanf("%lf",&f);
    scanf("%lf",&x);

   printf("Case #%d: %.7lf\n",l,leastTime(x,c,2.0,f));

}


return 0;}
