#include <bits/stdc++.h>
using namespace std;

int const maxn = 200;
char s[maxn][maxn];
int n,m;

bool good(char c, int i, int j)
{
    if (c == '^')
    {
        --i;
        while (i >= 0 && s[i][j] == '.')
            --i;
        return i >= 0;
    }
    if (c == '<')
    {
        --j;
        while (j >= 0 && s[i][j] =='.')
            --j;
        return j >= 0;
    }
    if (c == 'v')
    {
        ++i;
        while ( i < n && s[i][j] == '.')
            ++i;
        return i < n;
    }
    if (c == '>')
    {
        ++j;
        while (j < m && s[i][j] == '.')
            ++j;
        return j < m;
    }
    return true;
}

int main()
{
    freopen("inAL.txt","r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int T = 0;
    cin >> T;
    for(int tst = 1; tst <= T; ++tst)
    {
        cin >> n >> m;
        for(int i = 0; i < n; ++i)
            cin >> s[i];
        int ans = 0;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j)
            {
                if (!good(s[i][j],i,j))
                {
                    ++ans;
                    bool tmp = good('<',i,j) || good('>',i,j) || good('^',i,j) || good('v',i,j);
                    if (!tmp)
                    {
                        ans = -1000000000;
                    }

                }
            }
        if (ans < 0)
        {
            cout << "Case #" << tst << ": " << "IMPOSSIBLE\n";
        }
        else
        {
            cout << "Case #" << tst << ": " << ans << '\n';
        }
    }
    return 0;
}
