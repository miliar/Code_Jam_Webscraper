#include <stdio.h>

int main ()
{
    int T, A, B, K;
    scanf("%d", &T);
    for (int t = 0; t < T; ++t)
    {
        int count = 0;
        scanf("%d %d %d", &A, &B, &K);
        for (int i = 0; i < A; ++i)
        {
            for (int j = 0; j < B; ++j)
            {
                if ((i & j) < K)
                {
                    count++;
                }
            }
        }

        printf("Case #%d: %d\n", t+1, count);
    }
}