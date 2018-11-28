#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
using namespace std;

#define INT64 long long

int main()
{
    INT64 T;
    INT64 K, C, S;
    scanf("%lld", &T);
    for(INT64 t = 1; t <= T; t++)
    {
        scanf("%lld %lld %lld", &K, &C, &S);
        printf("Case #%lld:", t);
        if(C == 1)
        {
            if(S < K){
                printf(" IMPOSSIBLE\n");
                continue;
            }

            for (INT64 i = 1; i <= K; ++i)
            {
                printf(" %lld", i);
            }
            puts("");
        }

        else
        {
            INT64 first = 2;
            INT64 second = pow(K, C) - pow(K, C - 1);

            if(K == 2)
                printf(" %lld\n", first);

            else
            {
                if(S == 1)
                    printf(" IMPOSSIBLE\n");
                else
                    printf(" %lld %lld\n", first, second); 
            }
        }

    }
}