#include <cstdio>
#include <cstring>

const int N = 110;
char s[N][N];
int row[N], col[N];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) 
    {
        int n, m;
        scanf("%d%d", &n, &m);
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        for (int i = 0; i < n; ++i) scanf("%s", s[i]);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
            {
                if (s[i][j] != '.') row[i]++, col[j]++;
            }
        bool impossible = false;
        for (int i = 0; i < n && !impossible; ++i)
            for (int j = 0; j < m && !impossible; ++j)
                if (row[i] == 1 && col[j] == 1 && s[i][j] != '.') 
                {
                    //printf("%d %d\n", i, j);
                    impossible = 1;
                }
        printf("Case #%d: ", cas);
        if (impossible) 
        {
            puts("IMPOSSIBLE");
            continue;
        }
        int ans = 0;
        for (int i = 0; i < n; ++i)
        {
            if (row[i] == 0) continue;
            for (int j = 0; j < m; ++j)
                if (s[i][j] != '.') 
                {
                    if (s[i][j] == '<') ans++;
                    break;
                }
            for (int j = m - 1; j >= 0; --j)
                if (s[i][j] != '.')
                {
                    if (s[i][j] == '>') ans++;
                    break;
                }
        }
        for (int i = 0; i < m; ++i)
        {
            if (col[i] == 0) continue;
            for (int j = 0; j < n; ++j)
                if (s[j][i] != '.') 
                {
                    if (s[j][i] == '^') ans++;
                    break;
                }
            for (int j = n - 1; j >= 0; --j)
                if (s[j][i] != '.')
                {
                    if (s[j][i] == 'v') ans++;
                    break;
                }
        }
        printf("%d\n", ans);
    }
    return 0;
}
