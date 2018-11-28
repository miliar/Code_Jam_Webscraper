#include <stdio.h>

typedef unsigned long long uint64;

int sqrt (int remainder)
{
    if (remainder < 0)
        return 0; // negative number ERROR

    int place = (int)1 << (sizeof (int) * 8 - 2); // calculated by precompiler = same runtime as: place = 0x40000000
    while (place > remainder)
        place /= 4; // optimized by complier as place >>= 2

    int root = 0;
    while (place)
    {
        if (remainder >= root+place)
        {
          remainder -= root+place;
          root += place * 2;
        }
        root /= 2;
        place /= 4;
    }
    return root;
}

uint64 getDiv(uint64 n)
{
    for (int i = 2; i*i < n; ++i)
    {
        if (n%i == 0)
            return i;
    }

    return -1;
}

uint64 pow(int b, int e)
{
    if (e == 0)
        return 1;
    if (e % 2 == 0)
    {
        uint64 res = pow(b, e/2);
        return res * res;
    }
    uint64 res = pow(b, e/2);
    return res * res * b;
}

int main()
{
    int T, N, J;
    scanf("%d", &T);
    scanf("%d", &N);
    scanf("%d", &J);
    printf("Case #1:\n");
    uint64 n[11], d[11];
    for (int base = 2; base <= 10; ++base)
    {
        n[base] = 1 + pow (base, N-1);
    }

    int c = 0;
    while (c < J)
    {
        bool works = true;
        for (int base = 2; base <= 10; ++base)
        {
            uint64 divisor = getDiv(n[base]);
            if (getDiv(n[base]) == -1)
            {
                works = false;
                break;
            }
            d[base] = divisor;
        }

        if (works)
        {
            printf("%llu ", n[10]);
            for (int base = 2; base < 10; ++base)
            {
                printf("%llu ", d[base]);
            }
            printf("%llu\n", d[10]);
            c++;
        }

        n[2] += 2;
        int k = n[2];
        int bign[64];
        int index = 0;
        while (k > 0)
        {
            bign[index++] = k % 2;
            k /= 2;
        }

        for (int base = 3; base <= 10; ++base)
        {
            n[base] = 0;
            for (int i = N-1; i >= 0; --i)
            {
                n[base] = base * n[base] + bign[i];
            }
        }
    }
    return 0;
}