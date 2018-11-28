#include <cstdio>
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++ cas)
    {
        int n;
        long long p;
        scanf("%d%I64d", &n, &p);
        printf("Case #%d: ", cas);
        long long tot = 0;
        for (long long i = 1LL << (n - 1); i > 1; i /= 2)
            if ((p - 1) & i)
                tot += (1LL << n) / i;
            else
                break;
        if (p == (1LL << n))
            tot = p - 1;
        printf("%I64d ", tot);
        tot = (1LL << n) - 1;
        for (long long i = 2, x = (1LL << n) / 2; i <= p; i *= 2, x /= 2)
            tot -= x; 
        printf("%I64d\n", (1LL << n) - tot - 1);
    }
    return 0;
}
