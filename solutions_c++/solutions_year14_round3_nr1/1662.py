#include "rational.h"
#include <cstdio>
#include <iostream>
using namespace std;

int T;
long long P, Q;

int main()
{
    Rational unit(1, 2);
    Rational zero(0, 1);
    Rational data[45];
    data[1] = unit;
    for (int i = 2; i <= 40; i++)
        data[i] = data[i - 1] * unit;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int x = 1; x <= T; x++)
    {
        scanf("%lld/%lld", &P, &Q);
        Rational sum = Rational(P, Q);
        int ans = -1;
        for (int i = 1; i <= 40 && sum > zero; i++)
            if (sum >= data[i])
            {
                sum = sum - data[i];
                if (ans == -1)
                    ans = i;
            }
        if (sum > zero)
            ans = -1;
        printf("Case #%d: ", x);
        (ans == -1) ? puts("impossible") : printf("%d\n", ans);
    }
    return 0;
}
