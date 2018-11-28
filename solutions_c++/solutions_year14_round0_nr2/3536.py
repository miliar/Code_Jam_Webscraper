#include<cstdio>
#include<vector>
using namespace std;

double ans(double C,double F,double X)
{
    double t=0;
    double CF=2;
    while( C/CF+X/(CF+F)<X/CF )
    {
        t+=C/CF;
        CF+=F;
    }
    return t+X/CF;
}
int main()
{
    freopen("b_large.in","r",stdin);
    freopen("b_large.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=0;test<t;test++)

    {
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        printf("Case #%d: %.7lf\n",test+1,ans(C,F,X));
    }
    return 0;
}
