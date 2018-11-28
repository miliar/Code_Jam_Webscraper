#include <cstdio>

using namespace std;
int t,i;
double d,sol,c,x,f;
int main()
{
    freopen("gjamB.in","r",stdin);
    freopen("gjamB.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        d=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        sol=0;
        while(x/d>c/d+x/(d+f))
        {
            sol+=c/d;
            d+=f;
        }
        sol+=x/d;
        printf("Case #%d: %.7lf\n",i,sol);
    }
    return 0;
}
