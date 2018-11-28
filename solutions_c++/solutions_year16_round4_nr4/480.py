#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

const int N = 10;

int n;
char can[N][N + 1];
char new_can[N][N];
int perm[N];

bool good(int v, int mask)
{
    if (v == n)
        return true;
    bool any = false;
    for (int to = 0; to < n; to++)
    {
        if (new_can[perm[v]][to] == '0')
            continue;
        if (mask & (1 << to))
            continue;
        if (!good(v + 1, mask | (1 << to)))
            return false;
        any = true;
    }
    return any;
}

bool very_good()
{
    for (int i = 0; i < n; i++)
        perm[i] = i;
    do
    {
        if (!good(0, 0))
            return false;
    }
    while (next_permutation(perm, perm + n));
    return true;
}

void solve()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%s", can[i]);

    int best = (int)1e9;
    for (int mask = 0; mask < (1 << (n * n)); mask++)
    {
        int cost = 0;
        for (int i = 0; i < n * n; i++)
        {
            int r = i / n;
            int c = i % n;
            new_can[r][c] = can[r][c];
            if ((mask & (1 << i)) && can[r][c] == '0')
            {
                cost++;
                new_can[r][c] = '1';
            }
        }
        if (very_good())
            best = min(best, cost);
    }

    printf("%d\n", best);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }

    eprintf("time = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
