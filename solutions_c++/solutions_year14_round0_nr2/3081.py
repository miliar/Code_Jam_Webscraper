#include <iostream>
#include <cstdio>
using namespace std;
double ans;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    double C,F,X;
    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        ans=X/2.0;
        double nt=0;double nc=2.0;
        double wans;
        while(1)
        {
            nt+=C/nc;
            nc+=F;
            wans=nt+X/nc;
            if(wans>ans)break;
            else ans=wans;
        }
        printf("Case #%d: %.7lf\n",cs,ans);
    }
    return 0;
}
