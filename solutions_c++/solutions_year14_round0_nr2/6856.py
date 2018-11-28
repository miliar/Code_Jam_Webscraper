#include<stdio.h>
#include<algorithm>
#include<cmath>
using namespace std;
double c,f,x;

int pan(double n)
{
    double t=2;
    if (n*t>=x) return 1;
    while (n>=c/t){
        n-=c/t;
        t+=f;
        if (n*t>=x) return 1;
    }
    return 0;
}

int main()
{
     freopen("hehe.in","r",stdin);
     freopen("hello.out","w",stdout);
     int t;
     scanf("%d",&t);
     for (int k=1;k<=t;k++)
    {
        printf("Case #%d: ",k);
        scanf("%lf%lf%lf",&c,&f,&x);
        double l=0,r=100005;
        for (int i=1;i<=1000;i++){
        double mid=(l+r)*0.5;
        if (pan(mid)) r=mid;
        else l=mid;
        }
        printf("%.6lf\n",r);

    }
    return 0;
}
