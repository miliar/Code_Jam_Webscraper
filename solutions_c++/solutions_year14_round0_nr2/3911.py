#include<stdio.h>

int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        double time=0,cookie=0,r=2,c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        while(cookie<x)
        {
            time+=c/r;
            cookie+=c;
            if(((x-cookie)/r)<(x/(r+f)))
            {
                time+=(x-cookie)/r;
                cookie=x;
            }
            else
            {
                cookie=0;
                r+=f;
            }
        }
        printf("Case #%d: %lf\n",k,time);
    }
}
