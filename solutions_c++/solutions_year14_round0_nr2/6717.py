#include<iostream>
#include<stdio.h>
#include<iomanip>
using namespace std;
int main()
{
int t;
double x,c,f,time,old,rate,all,prev;
int tes=0;
scanf("%d",&t);
while(t--)
{
    tes++;

    cin>>c>>f>>x;
    rate=2;
    prev=0;
    old = x/2;

    if(x<=c)
    {
    printf("Case #%d: %0.7f\n",tes,x/rate);
    }
    else
    {
    while(1)
    {
    time=prev;
    time+=c/rate;
    prev=time;
    rate+=f;
    time+=x/rate;
    if(time>old)
    break;
    else
    old=time;
    }
    printf("Case #%d: %0.7f\n",tes,old);
    }


}

return 0;
}
