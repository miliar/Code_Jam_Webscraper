#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t; double C, F, X, T, a, old, n;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        old = X / 2;
        a = 0.5;
        n = 2 + F;
        T = C * a + X / n;
        while (T < old) {
            a += 1 / n;
            n += F;
            old = T;
            T = C * a + X / n;
            //printf("%lf\n", T);
        }
        printf("Case #%d: %.10lf\n", i, old);
    }
    return 0;
}
