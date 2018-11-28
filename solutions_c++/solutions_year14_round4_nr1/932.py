// vim:set sw=4 et smarttab:
// Round 2 2014

#include <cstdio>
#include <algorithm>

int n, x, s[10000];

int solve()
{
    std::sort(s, s + n);
    int i = 0, j = n - 1;
    int ret = 0;
    while (i <= j)
    {
        if (i == j)
        {
            ++ret;
            break;
        }
        else if (s[i] + s[j] > x)
        {
            --j;
            ++ret;
        }
        else
        {
            ++i, --j;
            ++ret;
        }
    }
    return ret;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; ++i)
            scanf("%d", &s[i]);
        int answer = solve();
        printf("Case #%d: %d\n", tc, answer);
    }
}
