// vim:set sw=4 et smarttab:
// Round 1C 2016

#include <cstdio>
#include <cassert>

int choice(const int a[], int n)
{
    int max = -1;
    int maxi = -1;
    for (int i = 0; i < n; ++i)
        if (a[i] > max)
            max = a[i], maxi = i;
    return maxi;
}

bool major(const int a[], int n, int total)
{
    for (int i = 0; i < n; ++i)
        if (2 * a[i] > total)
            return true;
    return false;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int n;
        scanf("%d", &n);
        int a[26] = {0, };
        int total = 0;
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &a[i]);
            total += a[i];
        }
        printf("Case #%d:", tc);
        while (total > 0)
        {
            int t = choice(a, n);
            printf(" %c", 'A' + t);
            --a[t];
            --total;
            if (major(a, n, total))
            {
                int t = choice(a, n);
                printf("%c", 'A' + t);
                --a[t];
                --total;
            }
            assert(!major(a, n, total));
        }
        printf("\n");
    }
}
