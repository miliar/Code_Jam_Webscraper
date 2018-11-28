#include <bits/stdc++.h>
typedef long long LL;
const int N = 1e5 + 10;
const int MAXN = 1e9 + 8;

using namespace std;

int n,k;
long double ans;
long double f[N];
long double p[N];
long double dp[N];

void solve()
{
    dp[0] = 1.0;
    //for(int i = 1;i <= k;i++) cout<<p[i]<<" ";cout<<endl;
    for(int i = 1;i <= k;i++)
    {
        dp[i] = 0.0;
        for(int j = i;j >= 1;j--)
        {
            dp[j] = dp[j] * (1.0 - p[i]) + dp[j - 1] * p[i];
        }
        dp[0] = dp[0] * (1.0 - p[i]);
    }
    ans = max(ans , dp[k / 2]);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T;
    cin>>T;
    for(int i = 1;i <= T;i++)
    {
        cin>>n>>k;
        for(int j = 1;j <= n;j++)
          cin>>f[j];
        sort(f + 1,f + n + 1);
        ans = 0.0;
        for(int j = 0;j <= k;j++)
        {//cout<<"!";
            int q = 0;
            for(int kk = 1;kk <= j;kk++) p[++q] = f[kk];
            for(int kk = n - k + j + 1;kk <= n;kk++) p[++q] = f[kk];
            solve();
        }

        double ANS = ans;
        printf("Case #%d: %.10f\n",i,ANS);
    }

    return 0;
}

