#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int x[1000], y[1000];
int mp[1000][1000];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int r = 1; r <= T; ++ r)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        memset(x, 0, sizeof(x));
        memset(y, 0, sizeof(y));
        for (int i = 0; i < n; ++ i)
            for (int j = 0; j < m; ++ j)
            {
                scanf("%d", &mp[i][j]);
                x[i] = max(x[i], mp[i][j]);
                y[j] = max(y[j], mp[i][j]);
            }
        bool flag = true;
        for (int i = 0; i < n; ++ i)
        {
            for (int j = 0; j < m; ++ j)
            {
                if (mp[i][j] < x[i] && mp[i][j] < y[j])
                {
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
        }
        printf("Case #%d: ", r);
        if (flag)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
