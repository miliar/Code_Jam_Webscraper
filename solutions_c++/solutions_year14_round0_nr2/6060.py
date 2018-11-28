#include <cstdio>

int cs;

inline void work() {
    double c, f, x, ans = 0;
    int i = 0;
    scanf("%lf%lf%lf", &c, &f, &x);
    for (; c / (2 + i * f) <= x / (2 + i * f) - x / (2 + (i + 1) * f); ++i)
        ans += c / (2 + i * f);
    printf("Case #%d: %.7f\n", ++cs, ans + x / (2 + i * f));
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--)
        work();
    return 0;
}
