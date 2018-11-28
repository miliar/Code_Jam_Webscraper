#include <cstdio>

double jizz() {
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);

    double ans = 1e9;
    double facc = 2;
    double tacc = 0;
    while (tacc < ans) {
        double cst = tacc + x / facc;
        if (cst < ans) ans = cst;

        tacc += c / facc;
        facc += f;
    }

    return ans;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
        printf("Case #%d: %.07f\n", t, jizz());

    return 0;
}
