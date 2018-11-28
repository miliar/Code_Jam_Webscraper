#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
using namespace std;
#define INFF 1000111222
double Min(double x,double y)
{
    return x<y?x:y;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ncase;
    int T=0;
    scanf("%d",&ncase);
    double c,f,x;
    while(ncase--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        int num=x*3;
        double ans=INFF;
        double t=c/2.0;
        double sum;
        for(int i=0;i<=num;i++)
        {
            if(i==0)
                t=0;
            else
                t=t+c/(2.0+(i-1)*f);
            sum=t+x/(2.0+i*f);
            ans=Min(ans,sum);
        }
        printf("Case #%d: %.7lf\n",++T,ans);
    }
    return 0;
}
