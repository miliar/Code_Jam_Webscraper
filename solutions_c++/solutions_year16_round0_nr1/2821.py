#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int T,cnt;
bool vis[10];
void calc(int x)
{
    int t;
    while(x)
    {
        t=x%10;
        x/=10;
        if(!vis[t])
        {
            vis[t]=1;
            ++cnt;
        }
    }
}
int main()
{
    LL n,ans;
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        cin>>n;
        printf("Case #%d: ",t);
        if(!n)
        {
            puts("INSOMNIA");
            continue;
        }
        memset(vis,0,sizeof(vis));
        cnt=0;
        calc(n);
        ans=n;
        while(cnt<10)
        {
            ans+=n;
            calc(ans);
        }
        cout<<ans<<endl;
    }
    return 0;
}
