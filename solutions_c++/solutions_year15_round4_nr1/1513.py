#include <cstdio>

int main()
{
    const int N = 0xFF;
    int T, r, c, up, down, left, right;
    scanf("%d", &T);
    for (int tst = 1; tst <= T; ++tst)
    {
        char map[N][N] = {0};
        scanf("%d%d ", &r, &c);
        for (int i = 1; i <= r; ++i)
            scanf("%s", map[i] + 1);
        int sum = 0, ok = 1;
        for (int i = 1; i <= r && ok; ++i)
        for (int j = 1; j <= c && ok; ++j)
        {
            if (map[i][j] == '.') continue;
            up = down = left = right = 0;
            for (int k = i - 1; k && !up; --k)
                up += map[k][j] != '.';
            for (int k = i + 1; k <= r && !down; ++k)
                down += map[k][j] != '.';
            for (int k = j - 1; k && !left; --k)
                left += map[i][k] != '.';
            for (int k = j + 1; k <= c && !right; ++k)
                right += map[i][k] != '.';
            if (map[i][j] == '^')
            {
                if (up) continue;
                if (down + right + left > 0) 
                    ++sum;
                else
                    ok = 0;
            }
            else if (map[i][j] == 'v')
            {
                if (down) continue;
                if (up + right + left > 0) 
                    ++sum;
                else
                    ok = 0;
            }
            else if (map[i][j] == '<')
            {
                if (left) continue;
                if (up + down + right > 0) 
                    ++sum;
                else
                    ok = 0;
            }
            else
            {
                if (right) continue;
                if (up + down + left > 0) 
                    ++sum;
                else
                    ok = 0;
            }
        }
        if (ok)
            printf("Case #%d: %d\n", tst, sum);
        else
            printf("Case #%d: IMPOSSIBLE\n", tst);
    }
    return 0;
}
