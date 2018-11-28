#include<cstdio>
#include<algorithm>
using namespace std;
const int MAXN=1005;
double naomi[MAXN],ken[MAXN];
int main()
{
    //freopen("D-small-attempt3.in","r",stdin);
    //freopen("D-small-attempt3.out","w",stdout);
    //freopen("D-large.in","r",stdin);
    //freopen("D-large.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas)
    {
        scanf("%d",&n);
        for(int i=0; i<n; ++i)
            scanf("%lf",&naomi[i]);
        for(int i=0; i<n; ++i)
            scanf("%lf",&ken[i]);
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int dwans=n,wans=0;
        for(int i=n-1,j=n-1; i>=0; --i)
            ken[i]>naomi[j]?--dwans:--j;
        for(int i=n-1,j=n-1; i>=0; --i)
            naomi[i]>ken[j]?++wans:--j;
        printf("Case #%d: %d %d\n",cas,dwans,wans);
    }
}
