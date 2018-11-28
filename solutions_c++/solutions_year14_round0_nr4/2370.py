#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int vis[20];
#define eps 1e-7
bool cmp(double a,double b)
{
    if(a-b<=eps) return true;
}
double a[1005],b[1005];
int use[1005];
int v1[1005];
int v2[1005];
int main()
{
    int cas;
    int ca=1;
    freopen("D-large.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    while(cas--)
    {
        int n;
        int f,k;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%lf",&a[i]);

        }
        for(int i=1;i<=n;i++)
        {
            scanf("%lf",&b[i]);

        }
        sort(a+1,a+1+n);
        sort(b+1,b+1+n);
        memset(use,0,sizeof(use));
        int ans1=n,ans2=n;
        for(int i=1;i<=n;i++)
        {
            int ok=0;
            for(int j=1;j<=n;j++)
            {
                if(use[j]) continue;
                if(b[j]>a[i])
                {
                    use[j]=1;
                    ok=1;
                    break;
                }
            }
            if(ok) ans2--;
        }
        memset(v1,0,sizeof(v1));
        memset(v2,0,sizeof(v2));
        int min1=1,min2=1,maxn1=n,maxn2=n;
        while(min1<=maxn1)
        {
            if(a[min1]<b[min2])
            {
                maxn2--;
                min1++;
                ans1--;
            }
            if(a[min1]>b[min2])
            {
                min1++;
                min2++;
            }
        }
        printf("Case #%d: %d %d\n",ca++,ans1,ans2);
    }
    return 0;
}
