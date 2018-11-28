#include <stdio.h>
#include <string.h>

char s[100][100];
int a[100][100][4];
bool used[100][100];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int n, m;

bool dfs(int x, int y, int &ans)
{
    int type = 0;
    if (s[x][y] == '^') { type = 3; }
    if (s[x][y] == 'v') { type = 2; }
    if (s[x][y] == '<') { type = 1; }
    if (s[x][y] == '>') { type = 0; }
    used[x][y] = true;

    if (a[x][y][type] != 0)
    {
        int nx = (a[x][y][type] - 1) / m, ny = (a[x][y][type] - 1) % m;
        if (used[nx][ny]) { return true; }
        else { return dfs(nx, ny, ans); }
    }

    int nx = -1, ny = -1;
    for (int i = 0; i < 4; i++)
    if (a[x][y][i] > 0)
    {
        nx = (a[x][y][i] - 1) / m;
        ny = (a[x][y][i] - 1) % m;
        break;
    }
    if (nx == -1)
    {
        return false;
    } else
    {
        ans = ans + 1;
        if (used[nx][ny]) { return true; }
        else { return dfs(nx, ny, ans); }
    }
}

int main()
{
    freopen("A-large.in","r", stdin);
    freopen("A-large.out","w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        printf("Case #%d: ", t);
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) { scanf("%s", s[i]); }
        memset(a, 0, sizeof(a));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
            if (s[i][j] != '.')
            {
                for (int k = 0; k < 4; k++)
                {
                    int x = i + dx[k], y = j + dy[k];
                    while ((x >= 0) && (x < n) && (y >= 0) && (y < m))
                    {
                        if (s[x][y] != '.')
                        {
                            a[i][j][k] = x * m + y + 1;
                            break;
                        }
                        x += dx[k];
                        y += dy[k];
                    }
                }
            }

        memset(used, false, sizeof(used));
        int ans = 0;
        bool ok = true;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if ((s[i][j] != '.') && (!used[i][j]))
                {
                    ok &= dfs(i, j, ans);
                }
        if (!ok) { printf("IMPOSSIBLE\n"); }
        else { printf("%d\n", ans); }
    }

    return 0;
}
