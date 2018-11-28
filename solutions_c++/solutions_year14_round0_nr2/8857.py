/*
Believe you can and you are halfway there.-Divyansh Sharma
*/
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<functional>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
using namespace std;
int main()
{
 int t,var=1;
 cin>>t;
while(var<=t)
{
    double C,F,X,v=2.0,compare_time=0.0,wt_time=0.0,next_time=0.0,time=0.0;
scanf("%lf%lf%lf",&C,&F,&X);
if(C>X)
    time=X/v;
else
{
    wt_time=C/v;
    compare_time=X/v;
    next_time=(X/(v+F));
while((wt_time+next_time)<compare_time)
{
    time+=wt_time;
     v+=F;
     wt_time=C/v;
     next_time=X/(v+F);
     compare_time=X/v;
}
time+=compare_time;
}
printf("Case #%d: %0.7lf\n",var,time);
var++;
}
return 0;
}
