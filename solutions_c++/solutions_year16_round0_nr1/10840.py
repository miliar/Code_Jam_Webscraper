#include <stdio.h>

int check[10];
long long N;
int checkN;

void input()
{
    int i;
    for (i = 0; i <= 9; ++i)
    {
        check[i] = 0;
    }
    checkN = 0;

    scanf("%lld", &N);
}

void process()
{
    int i = 0;
    long long targetN;
    if (N == 0)
    {
        printf("INSOMNIA\n");
    }
    else 
    {
        for (i = 1; i <= 100; ++i)
        {
            targetN = N * i;
            while (targetN)
            {
                if (check[targetN % 10] == 0)
                {
                    check[targetN % 10] = 1;
                    checkN++;
                }

                targetN /= 10;
            }
            
            if (checkN == 10)
                break;
        }
        if (checkN == 10)
            printf("%lld\n", N * i);
        else
            printf("INSOMNIA\n");
    }
}

int main(void)
{
    int i, T;
    scanf("%d", &T);
    
    for (i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        input();
        process();
    }

    return 0;
}
