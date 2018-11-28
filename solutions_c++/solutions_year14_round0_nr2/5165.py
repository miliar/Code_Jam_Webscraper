#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
for(int i=1;i<=t;i++)
{
    float c,f,x,a,b;
    float time=0,time1=0,time2=0;
    scanf("%f %f %f",&c,&f,&x);
    if(x<=c){
        time=x/2.0;
        //cout<<time;
        }
    else
    {
        time1=x/2.0;
        a=2.0;
        time=c/a;
        time2=x/(a+f);
    while(time+time2<time1)
    {
        time1=time+time2;
        a+=f;
        time+=c/a;
        time2=x/(a+f);
        /*b=c/(a+f);
        time1=x/a;
        if(b+time2<time1)
        {
            a+=f;
            time+=b;
            time2=b;
        }*/
    }
    time=time1;
    }
    printf("Case #%d: %f\n",i,time);
}
}
