#include <bits/stdc++.h>
typedef long long LL;
const int N = 100;
const int MAXN = 1e9 + 8;

using namespace std;

char _f[N][N];
bool f[N][N];
bool g[N][N];
int n,ans;
int a[N];

int l(int x) {return (x - 1) / n + 1;}
int r(int x) {return (x - 1) % n + 1;}

void check(int stu)
{
    int cost = 0;
    for(int j = 1;j <= n * n;j++)
    {
        g[l(j)][r(j)] = (stu & ( (1 << (j - 1)) )) > 0 ? 1 : 0;
        if(g[l(j)][r(j)] == 0 && f[l(j)][r(j)] == 1) return;
        if(g[l(j)][r(j)] == 1 && f[l(j)][r(j)] == 0) cost++;
    }

    bool dp[N];
    int res;

/*    cout<<"cost = "<<cost<<endl;
    for(int i = 1;i <= n;i++)
    {
        for(int j = 1;j <= n;j++) cout<<g[i][j];
        cout<<endl;
    }cout<<endl;*/

    for(int i = 1;i <= n;i++)
    {
        memset(dp,0,sizeof(dp));
        dp[0] = true;

        res = 0;
        for(int k = 1;k <= n;k++)
        if(g[i][k])
          res |= 1 << (k - 1);
        if(res == 0) //{cout<<"?"<<endl;}
          return;

        for(int j = 1;j <= n;j++)
        if(i != j)
        {
            for(int q = (1 << n) - 1;q >= 0;q--)
            if(dp[q] == 1)
            {
                for(int k = 1;k <= n;k++)
                if(g[j][k] == 1 && (q & (1 << (k - 1))) == 0)
                {
                    dp[q ^ (1 << (k - 1))] = 1;
                }
            }

            if(dp[res] == 1) //{cout<<i<<" "<<res<<endl;
            return;//}
        }
    }

    ans = min(ans , cost);
}

void solve()
{
    for(int i = 1;i <= 1 << (n * n);i++)
    {
        check(i);
    }
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);

    int T;
    cin>>T;
    for(int cas = 1;cas <= T;cas++)
    {
        cin>>n;
        ans = n * n;
        for(int i = 1;i <= n;i++)
        {
            scanf("%s",_f[i] + 1);
            for(int j = 1;j <= n;j++)
              f[i][j] = _f[i][j] - '0';
        }

        solve();

        printf("Case #%d: %d\n",cas,ans);
    }

    return 0;
}

