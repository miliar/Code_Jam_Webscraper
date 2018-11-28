// vim:set ts=8 sw=4 et smarttab:
// Qualification Round 2013

#include <cstdio>

int n, m;
int board[100][100];

bool possible_row(int i, int j)
{
    for (int j2 = 0; j2 < m; ++j2)
        if (board[i][j2] > board[i][j])
            return false;
    return true;
}

bool possible_col(int i, int j)
{
    for (int i2 = 0; i2 < n; ++i2)
        if (board[i2][j] > board[i][j])
            return false;
    return true;
}

bool possible(int i, int j)
{
    return possible_row(i, j) || possible_col(i, j);
}

bool solve()
{
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (!possible(i, j))
                return false;
    return true;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                scanf("%d", &board[i][j]);
        bool ans = solve();
        printf("Case #%d: %s\n", tc, ans ? "YES" : "NO");
    }
}
