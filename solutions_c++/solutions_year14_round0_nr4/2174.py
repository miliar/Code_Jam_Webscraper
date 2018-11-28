#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#define maxn 1009
using namespace std;
double a[maxn],b[maxn];
bool vis[maxn];
int main()
{
   // freopen("D.in","r",stdin);
    //freopen("DD.out","w",stdout);
    int tt,n,cot=1;
    scanf("%d",&tt);
    while(tt--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&b[i]);
        int ans1=0,ans2=0;
        sort(a,a+n);
        sort(b,b+n);
        memset(vis,0,sizeof(vis));
        for(int i=0;i<n;i++)
        {
            bool ok=0;
            for(int j=0;j<n;j++)
            {
                if(!vis[j]&&b[j]>a[i])
                {
                    vis[j]=1;
                    ok=1;
                    break;
                }
            }
            if(!ok)
            {
                for(int j=0;j<n;j++)
                {
                    if(!vis[j])
                    {
                        vis[j]=1;
                        ans2++;
                        break;
                    }
                }
            }
        }
        memset(vis,0,sizeof(vis));
        for(int i=0;i<n;i++)
        {
            bool ok=0;
            for(int j=0;j<n;j++)
            {
                if(!vis[j]&&a[j]>b[i])
                {
                    vis[j]=1;
                    ok=1;
                    ans1++;
                    break;
                }
            }
            if(!ok)
            {
                for(int j=0;j<n;j++)
                {
                    if(!vis[j])
                    {
                        vis[j]=1;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",cot++,ans1,ans2);
    }
}
