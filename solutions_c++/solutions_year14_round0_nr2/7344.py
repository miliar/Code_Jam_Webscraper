#include <cstdio>

const double EPS = 1e-10;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int test, cs;
    double c, f, x, r, t, t1, t2;
    scanf("%d", &test);
    for(cs = 1; cs <= test; cs++) {
        r = 2.0;
        t = 0.0;
        scanf("%lf %lf %lf", &c, &f, &x);
        while(true) {
            t1 = x / r;
            t2 = c / r + x / (r + f);
            if(t1 > t2 + EPS) {
                t += c / r;
                r += f;
            }
            else {
                t += x / r;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", cs, t + EPS);
    }
    return 0;
}
