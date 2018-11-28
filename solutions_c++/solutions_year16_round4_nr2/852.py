#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(long long i=a;i<b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define mod 1000000007
#define pi acos(-1)
#define eps 0.00000001
#define pb push_back

int n,t,k,use[22];
long double pp[222],p[222],dp[222][222],ans;

void calc()
{
    For(i,0,k+1) For(j,0,k+1) dp[i][j]=0;
    dp[0][0]=1;
    For(i,1,k+1)
    {
        dp[i][0] = dp[i-1][0]*p[i-1];
        For(j,1,k+1)
        {
            dp[i][j] = dp[i-1][j]*p[i-1] + dp[i-1][j-1]*(1-p[i-1]);
        }
    }
    ans=max(ans,dp[k][k/2]);
}

void solve()
{
    For(mask,3,1<<n) if(__builtin_popcount(mask)==k)
    {
        int j=0;
        For(i,0,n) if((1<<i)&mask)
        {
            p[j++]=pp[i];
        }
        calc();
    }
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin>>t;
    cout<<fixed<<setprecision(11);
    For(cas,1,1+t)
    {
        cout<<"Case #"<<cas<<": ";
        cin>>n>>k;
        For(i,0,n) cin>>pp[i];
        ans=0;
        reset(use,0);
        solve();
        cout<<ans<<endl;
    }
}
