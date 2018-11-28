#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxn = 11000;
char s[maxn];
pair<bool, char> ans[maxn][maxn];

pair<bool, char> mul(pair<int, char> a, char b)
{
    if (a.second == b)
    {
        return make_pair(!a.first, '1');
    }
    if (a.second == '1')
    {
        return make_pair(a.first, b);
    }
    a.first = a.first ^ (a.second > b) ^ (fabs(a.second - b) == 2);
    for (int c = 'i'; c <= 'k'; c ++)
    {
        if ((a.second != c) && (b != c))
        {
            return make_pair(a.first, c);
        }
    }
}

bool check(int l, int r, char target) {
    return ans[l][r].first && (ans[l][r].second == target);
}

int main()
{
    freopen("C-small1.in", "r", stdin);
    freopen("C-small1.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T ++)
    {
        bool flag = false;
        int l, x;
        scanf("%d %d", &l, &x);
        getchar();
        gets(s);
        for (int i = 1; i < x; i ++)
        {
            for (int j = 0; j < l; j ++)
            {
                s[i * l + j] = s[j];
            }
        }
        for (int limit1 = 0; limit1 < x * l; limit1 ++)
        {
            ans[limit1][limit1 + 1] = make_pair(true, s[limit1]);
            for (int limit2 = limit1 + 2; limit2 <= x * l; limit2 ++)
            {
                ans[limit1][limit2] = mul(ans[limit1][limit2 - 1], s[limit2 - 1]);
            }
        }
        for (int limit1 = 1; (limit1 < x * l - 1) && (!flag); limit1 ++)
        {
            if (!check(0, limit1, 'i'))
            {
                continue;
            }
            for (int limit2 = limit1 + 1; (limit2 < x * l) && (!flag); limit2 ++)
            {
                if (check(limit1, limit2, 'j') && check(limit2, x * l, 'k'))
                {
                    flag = true;
                }
            }
        }
        printf("Case #%d: %s\n", T, flag ? "YES" : "NO");
    }
    return 0;
}
