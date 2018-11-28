#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

long long power(int k, int c)
{
    long long res = 1;
    for (int i = 0; i < c; i++)
    {
        res *= k;
    }
    return res;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q;
    scanf("%d", &q);
    for (int t = 1; t <= q; ++t)
    {
        printf("Case #%d: ", t);
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        if (c == 1)
        {
            if (s < k)
            {
                printf("IMPOSSIBLE");
            }
            else
            {
                for (int i = 1; i <= k; i++)
                {
                    printf("%d ", i);
                }
            }
            printf("\n");
            continue;
        }
        if ((k + 1) / 2 > s)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for (int i = 1; i < k; i += 2)
        {
            printf("%d ", (i - 1) * k + i + 1);
        }
        if (k & 1)
        {
            printf("%d", k);
        }
        printf("\n");
    }
    return 0;
}