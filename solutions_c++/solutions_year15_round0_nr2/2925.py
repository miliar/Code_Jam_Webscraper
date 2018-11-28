#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<map>
#include<cmath>
using namespace std;
#define inf 0x3f3f3f3f
int a[1005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int i,j,t,n,mx,ca=1,sum,ans;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        mx=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            mx=max(mx,a[i]);
        }
        ans=inf;
        for(i=1;i<=mx;i++)
        {
            sum=0;
            for(j=0;j<n;j++)
            {
                if(a[j]>i)
                sum+=(a[j]-1)/i;
            }
            sum+=i;
            ans=min(ans,sum);
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}
