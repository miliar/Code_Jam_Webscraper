#include <iostream>
#include <string>
#include <cmath>

int T, N;
long long int r, t;
int main()
{
    scanf("%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        scanf("%lld %lld\n", &r, &t);

        long long int count = 0;
        for (long long int vol(r+r+1), sum(vol); sum <= t; sum = sum + vol) {
            vol = vol + 4;
            ++count;
        }
        printf("Case #%d: %lld\n", i, count);
    }
    return 0;
}

