#include<stdio.h>
double min,C,F,X;
void func(double prev,double rate)
{
    if(prev+(X/rate)<min)
        min=prev+(X/rate);
    if(prev+(C/rate)<min)
        func(prev+(C/rate),rate+F);
}
int main()
{
    int t,l;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        min=100000000;
        scanf("%lf%lf%lf",&C,&F,&X);
        func(0,2);
        printf("Case #%d: %lf\n",l,min);
    }
    return 0;
}
