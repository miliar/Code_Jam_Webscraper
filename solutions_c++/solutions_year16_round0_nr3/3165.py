#include <iostream>

using namespace std;
using ll = long long;

char rep[128];

void to_binary(ll n, int bits)
{
    rep[bits] = 0;

    for (int i = bits - 1; i >= 0; --i)
    {
        rep[i] = (n & 1) + '0';
        n >>= 1;
    }
}

int main()
{
    int T;
    scanf("%d", &T);

    int N, J;
    scanf("%d %d", &N, &J);

    ll mask = 1;
    ll base = (mask << N) - 1;

    printf("Case #%d:\n", T);

    while (J--)
    {
        ll coin = base;
        ll bits = 6; // 110
        ll m = mask;
 
        while (m)
        {
            if (m & 1)
                coin ^= bits;

            m >>= 1;
            bits <<= 2;
        }

        to_binary(coin, N);
        printf("%s", rep);

        for (int n = 2; n <= 10; ++n)
            printf(" %d", n + 1);

        printf("\n");

        ++mask;
    }

    return 0;
}
