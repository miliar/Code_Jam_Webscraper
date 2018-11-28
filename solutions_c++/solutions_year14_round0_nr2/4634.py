#include<cstdio>
#include<algorithm>
using namespace std;

double C,F,X,cps;

double notBuy()
{
    return X/cps;
}

double buy(int maxIter)
{
    if(maxIter==0) return notBuy();
    if(C>=X) return notBuy();
    maxIter--;
    double time = C/cps;
    cps += F;
    return time + min(buy(maxIter-1),notBuy());
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++)
    {
        cps = 2.0;
        scanf("%lf%lf%lf",&C,&F,&X);
        printf("Case #%d: %.7lf\n",tc,min(buy(50000),notBuy()));
    }
    return 0;
}
