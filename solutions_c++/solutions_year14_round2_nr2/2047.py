#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ri()
{
    int a;
    scanf("%i", &a);
    return a;
}

unsigned long long rl()
{
    unsigned long long a;
    scanf("%llu", &a);
    return a;
}

double rd()
{
    double a;
    scanf("%lf", &a);
    return a;
}

int main()
{
    int t, q=1;
    t = ri();
    while(t--)
    {
        int a, b, k, i, j;
        a = ri();
        b = ri();
        k = ri();
        unsigned long long qtd=0;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j)<k)
                {
                    qtd++;
                }
            }
        }
        printf("Case #%i: %llu\n", q++, qtd);
    }
    return 0;
}
