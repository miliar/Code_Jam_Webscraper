#include <stdio.h>

typedef unsigned long long uint64;

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
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        int K, C, S;
        scanf("%d %d %d", &K, &C, &S);
        printf("Case #%d: ", t);
        if (C == 1)
        {
            for (int i = 1; i < K; ++i)
            {
                printf("%d ", i);
            }
            printf("%d\n", K);
            continue;
        }
        else
        {
            for (uint64 i = 1; i+pow(K,C-1) < pow(K, C); )
            {
                printf("%llu ", i);
                i += pow(K,C-1);
            }
            printf("%llu\n", pow(K,C) + 1 - pow(K,C-1));
        }
    }
    return 0;
}