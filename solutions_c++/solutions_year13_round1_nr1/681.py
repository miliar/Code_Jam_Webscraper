#include <stdio.h>
#include <cmath>

void run(unsigned long long r, unsigned long long t)
{
    unsigned long long x = r + r + 1;
    unsigned long long low = 0;
    unsigned long long tmp = 1;

    while (low < tmp)
    {
        unsigned long long paint = (x + tmp + tmp) * (tmp + 1);

        if (paint == t)
        {
            break;
        }
        else if (paint < t)
        {
            low = tmp;
            tmp *= 2;
        }
        else
        {
            tmp = (low + tmp) / 2;
        }
    }

    printf("%llu\n", tmp + 1);

#if 0
    unsigned long long count = 0;
    unsigned long long paint = r + r + 1;
    unsigned long long total = paint;

    do {
        count++;
        paint += 4;
        total += paint;
    } while (total <= t);

    printf("%llu\n", count);
#endif
}

int main()
{
    int num_case;

    scanf("%d", &num_case);

    for (int i = 1; i <= num_case; ++i)
    {
        unsigned long long r, t;
        scanf("%llu %llu", &r, &t);

        printf("Case #%d: ", i);
        run(r, t);
    }

    return 0;
}
