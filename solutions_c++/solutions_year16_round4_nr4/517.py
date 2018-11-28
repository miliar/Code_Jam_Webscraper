#include <bits/stdc++.h>

using namespace std;

#define lol long long
#define fi first
#define se second
#define pb push_back
#define sz(s) (int)s.size()
#define must ios_base::sync_with_stdio(0)

#define inp(s) freopen(s, "r", stdin)
#define out(s) freopen(s, "w", stdout)

char c[5][5];
int used[5];
int usedp[5];
int mask;

bool check(int cur, int n)
{
    bool flag = true, start = false;
    if (cur == n)
    {
        for (int i = 0; i < n; i++)
            flag &= used[i];
        return flag;
    }
    for (int person = 0; person < n; person++)
        for (int i = 0; flag && i < n; i++)
            if (!used[i] && !usedp[person] && ((mask >> (person * n + i)) & 1))
            {
                used[i] = 1;
                usedp[person] = 1;
                start = true;
                flag &= check(cur + 1, n);
                used[i] = 0;
                usedp[person] = 0;
            }

    return flag && start;
}

int main()
{
    inp("input.txt");
    out("output.txt");
    int t, tt;
    scanf("%d", &t);
    for (tt = 1; tt <= t; tt++)
    {
        int n, i, j;
        scanf("%d\n", &n);
        for (i = 0; i < n; i++, scanf("\n"))
            for (j = 0; j < n; j++)
                scanf("%c", &c[i][j]);
        int ans = 100000;
        for (mask = 0; mask < (1 << (n * n)); mask++)
        {
            int res = 0;
            for (i = 0; i < n && res < ans; i++)
                for (j = 0; j < n && res < ans; j++) {
                    if (c[i][j] == '1' && ((mask >> (i * n + j)) & 1) == 0)
                        res = ans;
                    if (c[i][j] == '0' && ((mask >> (i * n + j)) & 1) == 1)
                        res++;
                }
            if (res > ans)
                continue;
            if (res < ans && check(0, n)) {
                ans = min(ans, res);
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
