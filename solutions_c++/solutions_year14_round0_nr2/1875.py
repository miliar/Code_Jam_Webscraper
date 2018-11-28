#include<stdio.h>
double func(double c, double r, double f, double x);
double mini(double a, double b);
int main()
{
    int i,t;
    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        double c,f,x,sum = 0,r;
        scanf("%lf %lf %lf",&c,&f,&x);
        r = 2;
        while(x/r > c/r + x/(r+f))
        {
            sum += c/r;
            r += f;
        }
        sum += x/r;
        printf("Case #%d: %.7lf\n",i,sum);
    }
    return 0;
}

double func(double c, double r, double f, double x)
{
    if(x/r < c/r + x/(r+f))
        return x/r;
    else
    {
        return mini(x/r, c/r + func(c,r+f,f,x));
    }
}

double mini(double a, double b)
{
    if(a < b)
        return a;
    return b;
}
