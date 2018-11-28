#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        double c,f,x,t=0.0,r=2.0,t1;
        scanf("%lf %lf %lf",&c,&f,&x);
        t1=x/2;
        //printf("%.7f",t1);
        while(true)
        {
            t=t+c/r;
            r=r+f;
            t=t+x/r;
            if(t>t1)
            {
                t=t1;
                break;
            }
            else
            {
                t1=t;
                t=t-x/r;
            }
        }
        printf("Case #%d: %.7f\n",i,t);
    }
}

