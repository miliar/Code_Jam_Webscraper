#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,cas,n,i,j,ans,a[1005],Max,div;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        ans=1005;
        for(i=1000;i>=1;i--)
        {
            div=0;
            for(j=0;j<n;j++)
            {
                if(a[j]%i)div+=a[j]/i;
                else div+=a[j]/i-1;
                //printf("[%d %d]\n",i,a[j]/i);
            }
            ans=min(div+i,ans);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
}
