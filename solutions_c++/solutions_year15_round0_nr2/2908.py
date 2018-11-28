#include <cstdio>

int n;
int a[1111];

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 0; kase < T; ++ kase) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++ i) {
            scanf("%d", &a[i]);
        }
        int res = 2222;
        for (int b = 1; b < 1111; ++ b) {
            int acc = 0;
            int c = 0;
            for (int i = 0; i < n; ++ i)
                if (a[i] > b) {
                    acc += (a[i] - b - 1) / b + 1;
                    c = b;
                } else {
                    if (a[i] > c) {
                        c = a[i];
                    }
                }
            if (acc + c < res) {
                res = acc + c;
            }
        }
        printf("Case #%d: %d\n", kase + 1, res);
    }
    return 0;
}
