#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)

int T;
int R, C;

int dx[256], dy[256];

char grid[105][105];
int col[105], row[105];

int main()
{
    dx['^'] = -1;
    dy['>'] = 1;
    dx['v'] = 1;
    dy['<'] = -1;

    scanf("%d", &T);
    REP(tc, T)
    {
        scanf("%d %d", &R, &C);
        REP(i, R)
            scanf("%s", grid[i]);

        memset(row, 0, sizeof row);
        memset(col, 0, sizeof col);

        REP(i, R) REP(j, C)
        {
            if (grid[i][j] != '.')
                row[i]++, col[j]++;
        }

        int res = 0;
        bool impossible = false;
        REP(i, R) REP(j, C)
        {
            if (grid[i][j] == '.')
                continue;

            int ni = i, nj = j;
            char a = grid[ni][nj];
            do
            {
                ni += dx[a];
                nj += dy[a];
            } while (ni >= 0 && ni < R && nj >= 0 && nj < C && grid[ni][nj] == '.');

            if (ni >= 0 && ni < R && nj >= 0 && nj < C)
                ;
            else if (row[i] == 1 && col[j] == 1)
            {
                impossible = true;
                break;
            }
            else
                res++;
        }
        if (impossible)
            printf("Case #%d: IMPOSSIBLE\n", tc+1);
        else
            printf("Case #%d: %d\n", tc+1, res);
    }
}
