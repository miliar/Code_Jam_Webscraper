#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    for (int cn = 1; cn <= t; cn++) {
        printf("Case #%d: ", cn);
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        if (c >= x) {
            printf("%.7lf\n", x / 2);
            continue;
        }
        double ans = 0;
        double s = 2;
        while (c*s + c*f < x*f) {
            ans += c / s;
            s += f;
        }
        printf("%.7lf\n", ans + x / s);
    }
}
