#include <iostream>
#include <array>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstdint>
#include <functional>
#include <intrin.h>

using namespace std;

int main(int argc, char **argv, char **envp)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T; cin >> T;

    for(int t = 0; t < T; ++t)
    {
        printf("Case #%d:\n", t + 1);

        int m, r, c;

        cin >> r >> c >> m;

        int field[7][7] = {0};

        std::uint32_t iter = 0;
        for(iter = 0; iter < (1 << (r * c)); ++iter)
        {
            if(__popcnt(iter) != m)
                continue;

            for(int j = 0; j < r * c; ++j)
                field[j / c + 1][j % c + 1] = bool(iter & (1 << j));

            if(m == r * c - 1)
            {
                for(int i = 0; i < r; ++i)
                {
                    for(int j = 0; j < c; ++j)
                    {
                        if(field[i + 1][j + 1])
                            printf("*");
                        else
                            printf("c");
                    }
                    printf("\n");
                }
                break;
            }

            int used[7][7] = {0};

#define N(x, y) (100 * field[x][y] + field[x - 1][y - 1] + field[x - 1][y] + field[x - 1][y + 1] + field[x][y - 1] + field[x][y + 1] + field[x + 1][y - 1] + field[x + 1][y] + field[x + 1][y + 1])

            std::function<int(int,int)> dfs = [&field, &used, &dfs, r, c](int i, int j)
            {
                if(i == 0 || j == 0 || i == r + 1 || j == c + 1 || used[i][j])
                    return 0;

                used[i][j] = 1;
                int v = N(i, j);
                int ow = 1;
                if(v == 0)
                {
                    ow += dfs(i - 1, j - 1);
                    ow += dfs(i - 1, j);
                    ow += dfs(i - 1, j + 1);

                    ow += dfs(i, j - 1);
                    ow += dfs(i, j + 1);

                    ow += dfs(i + 1, j - 1);
                    ow += dfs(i + 1, j);
                    ow += dfs(i + 1, j + 1);
                }
                return ow;
            };

            bool ok = false;

            for(int i = 1; i <= r; ++i)
            {
                for(int j = 1; j <= c; ++j)
                {
                    if(N(i, j) == 0)
                    {
                        int res = dfs(i, j);
                        if(res + m == r * c)
                        {
                            for(int c_i = 0; c_i < r; ++c_i)
                            {
                                for(int c_j = 0; c_j < c; ++c_j)
                                {
                                    if(i == c_i + 1 && j == c_j + 1)
                                        printf("c");
                                    else if(field[c_i + 1][c_j + 1])
                                        printf("*");
                                    else
                                        printf(".");
                                }
                                printf("\n");
                            }
                            i = 1000;
                            j = 1000;
                            ok = true;
                        }
                    }
                }
            }

            if(ok)
                break;
        }

        if(iter == (1 << (r * c)))
            printf("Impossible\n");
    }

    return 0;
}