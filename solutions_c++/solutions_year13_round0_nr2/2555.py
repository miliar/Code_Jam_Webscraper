#include <stdio.h>
#include <string.h>

bool solve(int n, int m, int field[200][200])
{
    bool cut_x[200], cut_y[200];
    memset(cut_x, false, sizeof(bool) * n);
    memset(cut_y, false, sizeof(bool) * m);
    int k = n * m;
    int last = 101;
    while (k != 0)
    {
        int max = -1;
        for (int i = 0; i != n; i++)
        {
            for (int j = 0; j != m; j++)
            {
                if ((field[i][j] < last) && (field[i][j] > max))
                {
                    max = field[i][j];
                }
            }
        }
        for (int i = 0; i != n; i++)
        {
            for (int j = 0; j != m; j++)
            {
                if ((field[i][j] == max) && cut_x[i] && cut_y[j])
                {
                    return false;
                }
            }
        }
        for (int i = 0; i != n; i++)
        {
            for (int j = 0; j != m; j++)
            {
                if (field[i][j] == max)
                {
                    cut_x[i] = true;
                    cut_y[j] = true;
                    k--;
                }
            }
        }
        last = max;
    }
    return true;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int n, m;
    int field[200][200];
    for (int k = 0; k != t; k++)
    {
        scanf("%d%d", &n, &m);
        for (int i = 0; i != n; i++)
        {
            for (int j = 0; j != m; j++)
            {
                scanf("%d", &field[i][j]);
            }
        }
        printf("Case #%d: %s\n", k + 1, solve(n, m, field) ? "YES" : "NO");
    }
    return 0;
}
