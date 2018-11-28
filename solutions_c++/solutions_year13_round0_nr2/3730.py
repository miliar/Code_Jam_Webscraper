#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
using namespace std;

int maze[110][110];
int cnt[110][110];
int ans, n, m;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int Case = 1; Case <= T; Case++)
    {
        ans = 1;
        memset(cnt, 0, sizeof(cnt));

        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &maze[i][j]);

        for (int i = 0; i < n; i++)
        {
            int Max = maze[i][0];
            for (int j = 1; j < m; j++)
                Max = max(Max, maze[i][j]);
            for (int j = 0; j < m; j++)
                if (maze[i][j] != Max)
                    cnt[i][j]++;
        }
        for (int i = 0; i < m; i++)
        {
            int Max = maze[0][i];
            for (int j = 1; j < n; j++)
                Max = max(Max, maze[j][i]);
            for (int j = 0; j < n; j++)
                if (maze[j][i] != Max)
                    cnt[j][i]++;
        }

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (cnt[i][j] == 2) ans = 0;

        if (ans)
            printf("Case #%d: YES\n", Case);
        else
            printf("Case #%d: NO\n", Case);
    }
    return 0;
}
