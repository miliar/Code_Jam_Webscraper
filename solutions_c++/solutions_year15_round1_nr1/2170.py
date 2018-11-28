#include<bits/stdc++.h>
using namespace std;
long long int ans=0,ans1=0;;
int n,i,a[1005],gap,t,X;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {X++;
    ans=0;
    ans1=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        gap=0;
        for(i=0;i<n-1;i++)
        {
            gap=max(gap,a[i]-a[i+1]);
            if(a[i+1]<a[i])
            {
                ans=ans+(a[i]-a[i+1]);
            }
        }
        ans1=0;
        for(i=0;i<n-1;i++)
        {
           ans1=ans1+min(a[i],gap);
        }
    printf("Case #%d: %lld %lld\n",X,ans,ans1);
    }
return 0;
}
