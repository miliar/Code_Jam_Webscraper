#include <cstdio>
#include <cstring>
double c, f, x;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        scanf("%lf %lf %lf", &c, &f, &x);
        if (c >= x) {
            printf("%.10lf\n", x / 2);
            continue;
        }
        double r = 2;
        double ans = c / r;
        while (1) {
            if ((x - c) / r <= x / (r + f)) break;
            else {
                r += f;
                ans += c / r;
            }
        }
        ans += (x - c) / r;
        printf("%.10lf\n", ans);

    }
    return 0;
}