// vim:set sw=4 et smarttab:
// Round 1C 2016

#include <cstdio>
#include <cassert>

typedef unsigned long long ull;

const int maxn = 50;
int n;
ull m;
bool adj[maxn][maxn];

bool solve()
{
    for (int i = 0; i < maxn; ++i)
        for (int j = 0; j < maxn; ++j)
            adj[i][j] = false;
    ull number_of_ways[maxn];
    for (int i = 0; i < maxn; ++i)
        number_of_ways[i] = 0;
    number_of_ways[n - 1] = 1;
    ull total = 0;
    int current = n - 1;
    while (true)
    {
        if (total + 1 >= m)
            break;
        --current;
        if (current == 0)
            return false;
        number_of_ways[current] = total + 1;
        for (int i = current + 1; i < n; ++i)
            adj[current][i] = true;
        total += total + 1;
    }
    while (m > 0)
    {
        assert(current > 0 && current < n);
        if (number_of_ways[current] <= m)
        {
            adj[0][current] = true;
            m -= number_of_ways[current];
        }
        ++current;
    }
    assert(m == 0);
    return true;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d%llu", &n, &m);
        printf("Case #%d: ", tc);
        if (solve())
        {
            printf("POSSIBLE\n");
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < n; ++j)
                    if (adj[i][j])
                        printf("1");
                    else
                        printf("0");
                printf("\n");
            }
        }
        else
            printf("IMPOSSIBLE\n");
    }
}
