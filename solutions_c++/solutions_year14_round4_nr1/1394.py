#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int T, n, m, a[11111], ans;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++)
    {
        scanf("%d%d", &n, &m);
        memset(a, 0, sizeof a);
        for (int i = 0, x; i < n; i++)
        {
            scanf("%d", &x);
            a[x]++;
        }
        ans = 0;
        for (int i = m; i > 0; i--)
            while (a[i] > 0)
            {
                a[i]--; ans++;
                for (int j = m - i; j > 0; j--)
                    if (a[j])
                    {
                        a[j]--; break;
                    }
            }
        printf("Case #%d: %d\n", tt + 1, ans);
    }
    return 0;
}
