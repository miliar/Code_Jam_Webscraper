#include<stdio.h>
#include<stdlib.h>
double c,f,x;
double mn(double a,double b)
{
    if(a>b)return b;
    return a;
}
double tc(double rate,int cnt)
{
    //now=x/rate;
    /*while((c/rate)+(x/(rate+f))+now<x/rate+now)
    {
        now=(c/rate);
        rate+=f;
    }*/
    //return x/rate;
    if(cnt>2000)return x/rate;
    else return mn((x/rate),(c/rate)+tc(rate+f,cnt+1));
}
main()
{
    int tt;
    scanf("%d",&tt);
    for(int ttt=0;ttt<tt;ttt++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("Case #%d: ",ttt+1);
        printf("%.7lf\n",tc(2,0));
    }
}
