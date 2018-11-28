#include <cstdio>

int main() {
    int T, n, p[1010], y, mx, tmp;
    scanf("%d", &T);
    for (int x = 1; x <= T; ++x) {
        scanf("%d", &n);
        mx = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &p[i]);
            if (p[i] > mx) mx = p[i];
        }
        y = mx;
        for (int i = 1; i < mx; ++i) {
            tmp = 0;
            for (int j = 0; j < n; ++j) {
                tmp += (p[j] / i);
                if (p[j] % i == 0) --tmp;
            }
            if (tmp + i < y) y = tmp + i;
        }
        printf("Case #%d: %d\n", x, y);
    }
    return 0;
}
