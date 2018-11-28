#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    double c, f, x;
    int T;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        scanf("%lf%lf%lf", &c, &f, &x);

        double k = floor((x * f / c - 2) / f - 1);

        if (k < 0) printf("Case #%d: %.7f\n", times + 1, x / 2);
        else {
            double sum = 0;
            for (int i = 0; i < k; i++) {
                sum += c / (2 + i * f);
            }

            double ans = min(sum + x / (2 + k * f), sum + c / (2 + k * f) + x / (2 + k * f + f));
            printf("Case #%d: %.7f\n", times + 1, ans);
        }
    }
}
