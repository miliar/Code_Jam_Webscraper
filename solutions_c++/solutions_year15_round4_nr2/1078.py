#include <cstdio>
#include <algorithm>
#define scanf(args...) (scanf(args) ? : 0)
typedef long double real;
const int MAXN = 100;
const real EPS = 1e-6;

std::pair<real, real> T[MAXN];

int main() {
    int t;
    scanf("%d", &t);

    for (int test=1; test<=t; test++) {
        int n;
        real v, x;
        scanf("%d%Lf%Lf", &n, &v, &x);

        for (int i=0; i<n; i++)
            scanf("%Lf%Lf", &T[i].first, &T[i].second);

        printf("Case #%d: ", test);

        if (n == 2) {
            real r1 = T[0].first, r2 = T[1].first;
            real c1 = T[0].second, c2 = T[1].second;

            if ((c1 > x && c2 > x) || (c1 < x && c2 < x))
                printf("IMPOSSIBLE\n");
            else if (std::abs(c1-c2) < EPS) {
                if (std::abs(x-c1) < EPS) 
                    printf("%.12Lf\n", v/(r1+r2));
                else
                    printf("IMPOSSIBLE\n");
            }
            else {
                real k1 = (v/r1)*(x-c2)/(c1-c2);
                real k2 = (v/r2)*(x-c1)/(c2-c1);

                printf("%.12Lf\n", std::max(k1, k2));
            }
        }
        else if (n == 1) {
            real r1 = T[0].first, c1 = T[0].second;
            real k1 = v/r1;

            if (std::abs(x-c1) < EPS)
                printf("%.12Lf\n", k1);
            else
                printf("IMPOSSIBLE\n");
        }
        else
            printf("UNKNOWN\n");

    }
}
