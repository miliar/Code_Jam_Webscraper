#include <stdio.h>

bool can_possible(long long n, long long p, long long x)
{
    long long left = (1 << n) - x + 1;
    long long best = 1 << n;
    while (left >= 2)
    {
        left /= 2;
        best /= 2;
    }
    return best <= p;
}

long long cal_possible(long long n, long long p)
{
    long long l = 1, r = 1 << n;
    while (l <= r)
    {
        int mid = (l + r) >>1;
        if (can_possible(n, p, mid)) l = mid + 1;
        else r = mid - 1;
    }
    return r - 1;
}

bool can_guarantee(long long n, long long p, long long x)
{
    long long left = x;
    long long best = 1;
    long long num = 1 << n - 1;
    while (left > 1)
    {
        left /= 2;
        best += num;
        num /= 2;
    }
    return best <= p;
}

long long cal_guarantee(long long n, long long p)
{
    long long l = 1, r = 1 << n;
    while (l <= r)
    {
        int mid = (l + r) >>1;
        if (can_guarantee(n, p, mid)) l = mid + 1;
        else r = mid - 1;
    }
    return r - 1;
}

int main()
{
    int T, cas = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        long long n, p;
        scanf("%I64d %I64d", &n, &p);
        printf("Case #%d: %I64d %I64d\n", cas,
               cal_guarantee(n, p), cal_possible(n, p));
    }
    return 0;
}
