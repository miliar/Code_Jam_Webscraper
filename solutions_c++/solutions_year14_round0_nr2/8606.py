#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
int x2,t;
scanf("%d",&t);
for(x2=1;x2<=t;x2++)
{
    double C,F,X,current_rate=2;
    cin>>C;
    cin>>F;
    cin>>X;
    double time=0;
    while(1)
        {
            if(X/current_rate<=((C/current_rate)+(X/(current_rate+F))))break;
            time+=C/current_rate;
            current_rate+=F;
        }
        time+=X/current_rate;
        printf("Case #%d: %.7lf\n",x2,time);
}
return 0;
}

