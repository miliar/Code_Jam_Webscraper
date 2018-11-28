# include <bits/stdc++.h>
using namespace std;
# define fi cin
# define fo cout
char s[10005];
int main(void)
{
    int t;
    fi>>t;
    int n;
    for (int j = 1;j <= t;++j)
    {
        fi>>n>>s;
        int cnt = 0;
        int ans = 0;
        for (int i = 0;i <= n;++i)
        if (s[i] != '0')
        {
            s[i] -= '0';
            if (i > cnt) ans += i - cnt,cnt += i - cnt;
            cnt += s[i];
        }
        fo << "Case #" << j << ": " << ans << '\n';
    }
}
