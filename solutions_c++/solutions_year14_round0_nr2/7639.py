#include <cstdio>
#include <vector>
#define P 1000000007
#define LL long long
using namespace std;
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cnt;
    double ans,x,a,d,y;
    scanf("%d",&cnt);
    for (int run=1;run<=cnt;run++)
    {
        a=2;ans=0;
        scanf("%lf%lf%lf",&x,&d,&y);
        while (y/a>x/a+x/d)
        {
            ans+=x/a;
            a+=d;
        }
        ans+=y/a;
        printf("Case #%d: %.7f\n",run,ans);

    }
    return 0;
}
