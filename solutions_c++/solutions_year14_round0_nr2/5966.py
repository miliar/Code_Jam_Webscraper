#include <cstdio>
#include <algorithm>

int main() {
    int test_count;
    scanf("%d", &test_count);
    for (int t = 1; t <= test_count; ++ t) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        double result = x / 2.;
        double total = 0;
        for (int i = 1; total < result; ++ i) {
            total += c / (2 + (i - 1) * f);
            result = std::min(result, total + x / (2 + i * f));
        }
        printf("Case #%d: %.7f\n", t, result);
    }
    return 0;
}
