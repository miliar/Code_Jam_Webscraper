#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int mat[105][105];
int minrH[105], maxrH[105];
int mincH[105], maxcH[105];

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    int t, n, m, cases = 1;
    scanf("%d", &t);
    while (t--)
    {
        for (int i = 0; i < 105; i++)
        {
            minrH[i] = mincH[i] = 105;
            maxrH[i] = maxcH[i] = 0;
        }
        int minH = 105;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                scanf("%d", &mat[i][j]);
                minH = minH < mat[i][j] ? minH : mat[i][j];
                minrH[i] = minrH[i] < mat[i][j] ? minrH[i] : mat[i][j];
                maxrH[i] = maxrH[i] > mat[i][j] ? maxrH[i] : mat[i][j];
                mincH[j] = mincH[j] < mat[i][j] ? mincH[j] : mat[i][j];
                maxcH[j] = maxcH[j] > mat[i][j] ? maxcH[j] : mat[i][j];
            }
        }

        int ok = 1;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (mat[i][j] == minH)
                {
                    if (minrH[i] == maxrH[i] || mincH[j] == maxcH[j])
                        continue;
                    ok = 0;
                    break;
                }
            }
        }

        printf("Case #%d: %s\n", cases++, ok ? "YES" : "NO");
    }
    return 0;
}
