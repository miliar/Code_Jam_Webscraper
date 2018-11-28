#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <utility>
#include <windows.h>
//#include <fun>
using namespace std;

double farmcost,farmoutput,goal,cookiepersec(2.0);

double rekurzija(double cookiepersecx,double sectogoal)
{
double tmp1(farmcost/cookiepersecx),tmp2(goal/(cookiepersecx+farmoutput));
double tmp( tmp1+ tmp2);
if(sectogoal>tmp) return rekurzija(cookiepersecx+farmoutput,tmp2)+tmp1;
else return sectogoal;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i(0);i<t;i++)
    {

    scanf("%lf %lf %lf",&farmcost,&farmoutput,&goal);
    double t=rekurzija (cookiepersec,goal/cookiepersec);

    printf("Case #%d: %.7lf\n",i+1,t);
    }
    return 0;
}
