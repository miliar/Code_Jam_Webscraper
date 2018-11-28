#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
double calc(double c,double x,double f,int k)
{
    double ans=0;
    double cc=0;
    for(int i=0;i<k;i++)
    {
        ans+=f/(2.0+cc);
        cc+=c;
    }
    ans+=x/(2+cc);
    return ans;
}
int main()
{
    int T=0;
    int M=0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&T);
    while(T--)
    {
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        int num=((F*X-2*C)/(F*C));
        printf("Case #%d: %.7f\n",++M,calc(F,X,C,num));
    }
}
