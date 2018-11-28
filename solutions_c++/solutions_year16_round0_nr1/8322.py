#include<bits/stdc++.h>
#define ll long long
using namespace std;

bool vis[11];

bool test(ll n)
{
    while(n!=0)
    {
        vis[n%10]=true;
        n/=10;
    }
    for(int i=0;i<10;i++)
        if(!vis[i])
            return false;
    return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        ll n,cnt=1,ans;
        scanf("%lld",&n);
        ans=n;
        memset(vis,false,sizeof vis);
        if(!n)
        {
            printf("Case #%d: INSOMNIA\n",cases);
            continue;
        }
        while(!test(n*cnt))
        {
            //cout<<cnt<<" "<<ans<<endl;
            cnt++;
            ans = n*cnt;

        }
        printf("Case #%d: %lld\n",cases,ans);
    }

    return 0;
}
