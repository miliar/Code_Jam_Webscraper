#include<bits/stdc++.h>
using namespace std;
#define maxi 1005

int main()
{
    int t,n;
    long long int a[maxi],ans1,ans2,m;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%d ",&a[i]);
        ans1=ans2=m=0;
        for(int i=1;i<n;i++)
        {
            if(a[i-1]-a[i]>0)
            ans1+=(a[i-1]-a[i]);
            m=max(m,a[i-1]-a[i]);
        }
        for(int i=0;i<n-1;i++)
        ans2+=min(a[i],m);
        printf("Case #%d: %lld %lld\n",k,ans1,ans2);
    }
    return 0;
}
