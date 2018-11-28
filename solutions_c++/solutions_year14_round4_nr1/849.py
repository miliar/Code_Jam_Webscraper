#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int T,n,m,a[10005];
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    scanf("%d",&T);
    for(int I=1;I<=T;++I)
    {
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;++i) scanf("%d",&a[i]);
        sort(a+1,a+n+1); int ans=0;
        for(int i=n,j=1;i>=j;--i,++ans)
            if(a[i]+a[j]<=m&&i!=j) ++j;
        printf("Case #%d: %d\n",I,ans);
    }
    return 0;
}
