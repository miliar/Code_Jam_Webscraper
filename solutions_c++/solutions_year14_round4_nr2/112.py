#include <cstdio>
#include <algorithm>
using namespace std;
int a[1010];
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int n;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        int l=1,r=n,ans=0;
        for (int i=1;i<=n;i++)
        {
            int t=l;
            for (int j=l;j<=r;j++)
                if (a[j]<a[t])
                    t=j;
            if (t-l<=r-t)
            {
                for (int j=t;j>l;j--)
                {
                    ans++;
                    swap(a[j],a[j-1]);
                }
                l++;
            }
            else
            {
                for (int j=t;j<r;j++)
                {
                    ans++;
                    swap(a[j],a[j+1]);
                }
                r--;
            }
        }
        static int id=0;
        printf("Case #%d: %d\n",++id,ans);
    }
    return(0);
}

