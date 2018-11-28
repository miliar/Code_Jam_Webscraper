#include<iostream>
#include<vector>
#include<cstdio>
#include<queue>
#include<cstring>
using namespace std;
long long dp[1000001];
void init()
{
    long long i,j,a[10],br,b;
    for(i=1;i<=1000001;++i)
    {
        memset(a,0,sizeof(a));
        br=0;
        for(j=1;br<10;++j)
        {
            b=j*i;
            if(b<0)
            {
                cout<<b<<endl;
                return;
            }
            while(b)
            {
                if(a[b%10]==0)
                {
                    ++a[b%10];
                    ++br;
                }
                b/=10;
            }
        }
        dp[i]=j-1;
    }
}
void solve()
{
    int x;
    cin>>x;
    if(x==0)cout<<"INSOMNIA\n";
    else cout<<dp[x]*x<<'\n';
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int i,n;
    init();
    cin>>n;
    for(i=1;i<=n;++i)
    {
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
