#include <stdio.h>
#include <algorithm>

int n,m,a[102][102],maxR[102],maxC[102];
using namespace std;

void solve()
{
    int i,j;

    for(i=1;i<=n;++i) maxR[i]=0;
    for(i=1;i<=m;++i) maxC[i]=0;

    for(i=1;i<=n;++i) for(j=1;j<=m;++j)
    {
        if(a[i][j]>maxR[i]) maxR[i] = a[i][j];
        if(a[i][j]>maxC[j]) maxC[j] = a[i][j];
    }
    for(i=1;i<=n;++i) for(j=1;j<=m;++j)
        if(a[i][j] != min(min(maxR[i],maxC[j]),100) )
        {
            printf("NO\n");
            return;
        }
    printf("YES\n");
}

int main()
{
    freopen("bb.in","r",stdin);
    freopen("bb.out","w",stdout);
    int i,j,k,t,T=0;

    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;++i) for(j=1;j<=m;++j) scanf("%d",&a[i][j]);

        printf("Case #%d: ",++T);
        solve();
    }

    return 0;
}
