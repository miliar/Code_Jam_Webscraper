#include <iostream>
#include <cstdio>

using namespace std;
const double OO = 1e300;

double C,F,X;

double ins;
double nowGo;
double nextGo;
double cost;

int main()
{
    int T;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    int cas=0;
    while (T--){
        ins=2.0;
        cost=0;
        scanf("%lf%lf%lf",&C,&F,&X);
        nowGo=cost+X/ins;
        nextGo=cost+C/ins+X/(ins+F);
        while (nextGo<nowGo){
            cost+=C/ins;
            ins+=F;
            nowGo=cost+X/ins;
            nextGo=cost+C/ins+X/(ins+F);
        }
        printf("Case #%d: %.7f\n",++cas,nowGo);
    }
    return 0;
}
