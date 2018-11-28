#include <stdio.h>

int n = 32;
int m = 500;

long long proof[12];

bool check(long long a)
{
    for (int base = 2; base <= 10; ++ base)
    {
        bool ok = false;
        for (int div = 2; div <= 100; ++ div)
        {
            int rem = 0;
            for(int i = 0; i < n; ++ i)
            {
                rem *= base;
                if (a & (1 << (n - 1 - i)))
                {
                    rem ++;
                }
                rem %= div;
            }
            if (rem == 0)
            {
                proof[base] = div;
                ok = true;
                break;
            }
        }
        if (!ok) return false;
    }
    return true;
}

int main()
{
    printf("Case #1:\n");

    long long q = (1ll << (n - 1)) + 1;
    while (m)
    {
        if (check(q))
        {
            for (int i = 0; i < n; ++ i) {
                printf("%d", (q & (1 << (n - 1 - i))) ? 1 : 0);
            }
            for (int base = 2; base <= 10; ++ base)
            {
                printf(" %lld", proof[base]);
            }
            printf("\n");
            -- m;
        }
        q += 2;
    }

    return 0;
}

