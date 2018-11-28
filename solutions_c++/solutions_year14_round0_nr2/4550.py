#include <iostream>
#include <fstream>
#include <cstdio>
#include <string.h>
using namespace std;

int main() {
    freopen("tb_large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    int t;
    double c, f, x, r, ans, cur;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++) {
        scanf("%lf%lf%lf", &c, &f, &x);
        r = 2.0;
        ans = 0.0;
        cur = 0.0;
        while (cur < x) {
            if (cur < c) {
                if (x <= c) {
                    ans += ((x - cur) / r);
                    cur = x;
                } else {
                    ans += ((c - cur) / r);
                    cur = c;
                }
            } else {
                if ((x - cur) * (r + f) > (x - cur + c) * r) {
                    r += f;
                    cur -= c;
                } else {
                    x -= cur;
                    cur = 0;
                }
            }
        }
        printf("Case #%d: %.7lf\n", z, ans);
    }
    return 0;
}
