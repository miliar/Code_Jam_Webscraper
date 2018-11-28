#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

const int N = 16;

int n, k;
double prob[N];

void solve()
{
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%lf", &prob[i]);

    double best = 0;
    for (int mask = 0; mask < (1 << n); mask++)
    {
        if (__builtin_popcount(mask) != k)
            continue;
        double sum = 0;
        for (int sub = mask; sub > 0; sub = mask & (sub - 1))
        {
            if (__builtin_popcount(sub) != k / 2)
                continue;
            double P = 1;
            for (int i = 0; i < n; i++)
            {
                if (!(mask & (1 << i)))
                    continue;
                if (sub & (1 << i))
                    P *= prob[i];
                else
                    P *= 1 - prob[i];
            }
            sum += P;
        }
        best = max(best, sum);
    }

    printf("%.10lf\n", best);
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
