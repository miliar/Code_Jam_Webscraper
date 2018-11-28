#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A1-large.in","r",stdin);
    freopen("As.txt","w",stdout);
    int t,n,a[1005],cas,Max,i;
    long long f,s;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        f=0,s=0,Max=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            if(i&&a[i-1]>a[i])f+=a[i-1]-a[i];
            if(i&&a[i-1]>a[i]&&a[i-1]-a[i]>Max)Max=a[i-1]-a[i];
        }
        for(i=0;i<n-1;i++)
        {
            s+=min(a[i],Max);
        }
        printf("Case #%d: %lld %lld\n",cas,f,s);
    }
}
