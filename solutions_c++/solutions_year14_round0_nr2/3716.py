#include<iostream>
#include<cstdio>
using namespace std;
const double eps = 1e-8;
double C,F,X,now,sum,ans;

int main()
{
    freopen("B-large.in","rb",stdin);
    freopen("test.out","wb",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",cas++);
        scanf("%lf%lf%lf",&C,&F,&X);
        now=2.;ans=0.;
        for(;X*F-C*now-C*F>-eps;now+=F){
            ans+=C/now;
        }
        if(X*F<C*now+C*F) ans+=X/now;
        printf("%.7lf\n",ans);
    }
    return 0;
}
