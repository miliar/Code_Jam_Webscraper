#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;
ll num[11];

int main()
{
    freopen("C_large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        int N, J;
        scanf("%d %d", &N, &J);

        printf("Case #%d:\n", Ti);

        for(int i = 2; i <= 10; i++)
        {
            num[i] = 1;

            for(int Ni = 0; Ni < N; Ni+=2)
                num[i] *= i;

            num[i] += 1;
        }

        for(int Ji = 0; Ji < J; Ji++)
        {
            ll p = (1LL<<(N/2-1) )+Ji*2+1;

            for(int i = 0; i < 2; i++)
                for(ll vi = 1LL<<(N/2-1), Ni = 0; Ni < N; Ni+=2, vi/=2)
                    if( p&vi ) putchar('1');
                    else putchar('0');

            for(int i = 2; i <= 10; i++)
                printf(" %lld", num[i]);
            puts("");
        }
    }
}
