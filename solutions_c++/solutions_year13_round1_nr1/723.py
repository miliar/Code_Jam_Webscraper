#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int T;
    long long r, v;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lld %lld", &r, &v);
        long double x = 2 * r + 1;

        long double a = 2;
        long double b = x - 2;
        long double c = -v;

        long double delta = b * b - 4 * a * c;

        long double s0 = (-b + sqrtl(delta)) / (2 * a);

        long long k = floorl(s0);
        if (2 * k * k + (x - 4) * k - v > 0)
            k--;

        printf("Case #%d: %lld\n", t, k);
    }
}
