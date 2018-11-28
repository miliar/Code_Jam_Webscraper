#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
double a[1010],b[1010];
bool use[1010];
int cheat(int n)
{
    int l=1,r=n,ans=0;
    for (int i=1;i<=n;i++)
        if (a[i]<b[l])
            r--;
        else
        {
            ans++;
            l++;
        }
    return(ans);
}
int normal(int n)
{
    int ans=0;
    memset(use,0,sizeof(use));
    for (int i=1;i<=n;i++)
    {
        int t=-1;
        for (int j=1;j<=n;j++)
            if (!use[j] && a[i]<b[j])
            {
                t=j;
                break;
            }
        if (t==-1)
        {
            ans++;
            for (int j=1;j<=n;j++)
                if (!use[j])
                {
                    use[j]=true;
                    break;
                }
        }
        else
            use[t]=true;
    }
    return(ans);
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int n;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
            scanf("%lf",&a[i]);
        for (int i=1;i<=n;i++)
            scanf("%lf",&b[i]);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        static int id=0;
        printf("Case #%d: %d %d\n",++id,cheat(n),normal(n));
    }
    return(0);
}

