#include <bits/stdc++.h>

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t, s;
    double cps, c, f, x, telap;
    scanf("%d", &t);
    for (s=1; s <= t; s++) {
        telap = 0.0;
        cps = 2.0;
        scanf("%lf %lf %lf", &c, &f, &x);
        while ((x / cps) > (c / cps) + (x / (cps + f))) {
            telap += (c / cps);
            cps += f;
        }
        telap += (x / cps);
        printf("Case #%d: %.7lf\n", s, telap);
    }
    return 0;
}
