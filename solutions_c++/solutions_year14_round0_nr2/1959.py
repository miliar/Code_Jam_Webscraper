#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int round=0,r=1;
    double rate=2,cost=0,incrate=0,goal=0,curtime=0,lasttime=0,costtime=0;
    scanf("%d",&round);
    while(r<=round){
        scanf("%lf %lf %lf",&cost,&incrate,&goal);
        curtime=0,lasttime=0,rate=2,costtime=cost/rate;
        lasttime=goal/rate;
        while(1){
            rate+=incrate;
            curtime=goal/rate+costtime;
            costtime+=cost/rate;
            if(curtime>=lasttime)
                break;
            else lasttime=curtime; 
        }
        printf("Case #%d: %.7lf\n",r,lasttime);
        r++;
    }
    return 0;
}
