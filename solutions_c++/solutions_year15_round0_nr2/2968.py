# include <bits/stdc++.h>
# define fi cin
# define fo cout
using namespace std;
int s[1005];
int main(void)
{
    int t,n;
    fi>>t;
    for (int j = 1;j <= t;++j)
    {
        fi>>n;
        int ans = INT_MAX;
        int cnt = 0;
        for (int i = 1;i <= n;++i) fi>>s[i],cnt = max(cnt,s[i]);
        for (int x = 1;x <= cnt;++x)
            {
                int c = 0;
                for (int y = 1;y <= n;++y)
                   c += (s[y] - 1) / x;
                ans = min(ans,c + x);
            }
        fo << "Case #" << j << ": " << ans << '\n';
    }
    return 0;
}
