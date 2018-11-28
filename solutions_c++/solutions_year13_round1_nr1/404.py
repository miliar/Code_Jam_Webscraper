#include <cstdio>
#include <algorithm>
long long r, q;
bool f(long long k)
{
    return 2 * k - 1 + 2 * r <= q / k;
}
long long ub(long long a, long long b)
{
    long long k = (a + b) / 2;
    if(a == b)
        return a;
    if(b - a == 1)
    {
        if(f(b))
            return b;
        return a;
    }
    if(f(k))
        return ub(k, b);
    return ub(a, k - 1);
}
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    long long t, i;
    scanf("%lld", &t);
    for(i = 1; i <= t; i++)
    {
        scanf("%lld%lld", &r, &q);
        printf("Case #%lld: %lld\n", i, ub(1, 5000000000000000000LL));
    }
    return 0;
}
