#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;
int main()
{
 
int T;
double C,F,X;
 

scanf("%d",&T);
int t=1;
while(T--){
 
scanf("%lf %lf %lf",&C,&F,&X);
 
double r1 = 0;
double a1 = 2;
 
while(1){
 
double t1 = X/a1;
double t2 = ( C / a1 )+( X / ( F+a1 ) );
 
if(t2 < t1 ){

r1+=(C/a1);

a1+=F;
}
else
{
r1+=X/a1;
break;
}
 
}
printf("Case #%d: %.7lf\n",t,r1);
t++;
 
}
 
return 0;
}
