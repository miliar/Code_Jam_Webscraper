#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++)
    {
        int K, C, S;
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", c);
        long long kc = 1;
        for (int i = 0; i < C; i++)
        {
            kc *= K;
        }
        if (kc == 1)
        {
            printf(" 1");
        }
        else
        {
            for (long long i = 1; i <= kc; i+= (kc - 1) / (K - 1))
            {
                printf(" %lld", i);
            }
        }
        printf("\n");
    }
    return 0;
}

