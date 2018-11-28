#include <cstdio>

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    double c, f, x, cur, tot, ret;

    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        scanf("%lf%lf%lf", &c, &f, &x);

        if (x < c) {
            printf("Case #%d: %lf\n", cas, x / 2);
            continue;
        }

        cur = 2;
        tot = ret = 0;
        while (tot < x) {
            if (tot >= c) {
                if (x / (cur + f) < (x - tot) / cur) {
                    tot -= c;
                    cur += f;
                }
                else {
                    ret += (x - tot) / cur;
                    break;
                }
            }
            else {
                ret += (c - tot) / cur;
                tot = c;
            }
        }
        printf("Case #%d: %.8lf\n", cas, ret);
    }

    return 0;
}
