# include <bits/stdc++.h>
using namespace std;
# define fi cin
# define fo cout
# define x first
# define y second
# define ll long long
# define db long double
# define scn(x) scanf("%I64d",&x)
# define scan(x) scanf("%d",&x)
# define print(x) printf("%d ",x)
# define prnt(x) printf("%I64d ",x);
# define eol printf("\n")
# define IOS ios_base :: sync_with_stdio(0)
# define pe "Possible"
# define ie "Impossible"
# define halt(...) {fo << (__VA_ARGS__) << '\n';exit(0);}
# define rep(n) for (int qwerty = 1;qwerty <= n;++qwerty)
# define pp(n) cerr << #n << " = " << n << '\n'
# define ppp(v) for (auto it : v) cerr << it << ' ';cerr << '\n'
const int mod = 1e9 + 7;
db dp[18][18];
db s[205];
int main(void)
{
    int t;
    ifstream fi("input");
    ofstream fo("output");
    fi>>t;
    for (int cs = 1;cs <= t;++cs)
    {
        int n,k;
        fi>>n>>k;
        k /= 2;
        db ans = 0;
        for (int i = 1;i <= n;++i) fi>>s[i];
        for (int mask = 0;mask < (1 << n);++mask)
            if (__builtin_popcount(mask) == k+k)
            {
                memset(dp,0,sizeof(dp));
                dp[0][0] = 1;
                int was = 0;
                for (int q = 1;q <= n;++q)
                    if ((mask >> (q - 1)) & 1)
                    {
                        ++was;
                        for (int i = 0;i <= min(was,k);++i)
                            dp[i][was - i] += (1 - s[q]) * dp[i][was - i - 1] + s[q] * dp[i - 1][was - i];
                    }
                ans = max(ans,dp[k][k]);
            }
        fo << "Case #" << cs << ": " << fixed << setprecision(6) << ans << '\n';
    }
    return 0;
}


