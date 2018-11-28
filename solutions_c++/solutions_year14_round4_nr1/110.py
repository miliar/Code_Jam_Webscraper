#include <cstdio>
#include <algorithm>
using namespace std;
int a[10010];
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        int ans=0,l=1,r=n;
        while (l<=r)
        {
            ans++;
            if (l<r && a[l]+a[r]<=m)
                l++;
            r--;
        }
        static int id=0;
        printf("Case #%d: %d\n",++id,ans);
    }
    return(0);
}

