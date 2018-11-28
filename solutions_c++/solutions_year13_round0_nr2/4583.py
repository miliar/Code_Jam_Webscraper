#include <stdio.h>
#include <algorithm>
using namespace std;

int r[110], c[110], a[110][110];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, n, m;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; ++i)
        {
            r[i] = 0;
        }
        for (int j = 0; j < m; ++j)
        {
            c[j] = 0;
        }

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                scanf("%d", &a[i][j]);
                r[i] = max(r[i], a[i][j]);
                c[j] = max(c[j], a[i][j]);
            }
        }

        bool isValid = true;
        for (int i = 0; isValid && i < n; ++i)
        {
            for (int j = 0; isValid && j < m; ++j)
            {
                if (a[i][j] != min(r[i], c[j]))
                {
                    isValid = false;
                }
            }
        }

        printf("Case #%d: %s\n", cas, isValid ? "YES" : "NO");
    }
    return 0;
}
