#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

typedef long long LL;

LL bp[20][20];

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    for(LL i = 2; i <= 10; i++)
        bp[i][0] = 1;
    for(LL i = 2; i <= 10; i++)
        for(LL j = 1; j <= 16; j++)
            bp[i][j] = bp[i][j - 1] * i;

    LL T;
    scanf("%lld", &T);
    for(LL test = 1; test <= T; test++)
    {
        LL N, D;
        scanf("%lld%lld", &N, &D);

        printf("Case #%lld:\n", test);

        for(LL msk = 0; msk < 1 << (N - 2); msk++)
        {
            LL nr[15] = {0};
            for(LL j = 2; j <= 10; j++)
                nr[j] = 1 + bp[j][N - 1];

            for(LL bit = 0; bit < N - 2; bit++)
                if(msk & (1LL << bit))
                {
                    for(LL j = 2; j <= 10; j++)
                        nr[j] += bp[j][bit + 1];
                }

            LL pr[15] = {0};
            LL ok = 1;
            for(LL j = 2; j <= 10; j++)
            {
                LL K = nr[j];
                LL prm = 1;
                for(LL i = 2; i * i <= K; i++)
                    if(K % i == 0)
                    {
                        prm = i;
                        break;
                    }
                if(prm == 1)
                {
                    ok = 0;
                    break;
                }

                pr[j] = prm;
            }

            if(!ok) continue;



            printf("1");
            for(LL bit = N - 3; bit >= 0; bit--)
            {
                if(msk & (1LL << bit))
                    printf("1");
                else
                    printf("0");
            }

            printf("1 ");
            for(LL i = 2; i <= 10; i++)
                printf("%lld ", pr[i]);
            printf("\n");

            D--;
            if(D == 0)
                break;
        }
    }
    return 0;
}
