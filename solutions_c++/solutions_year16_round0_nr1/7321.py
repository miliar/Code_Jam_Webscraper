#include <cstdio>

int main() {
    int T;

    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        int n;
        scanf("%d", &n);
        if (!n) {
            printf("Case #%d: INSOMNIA\n", kase);
            continue;
        }
        int vis[10];
        for (int i = 0; i < 10; i++) vis[i] = 0;
        int exist = 0;
        int cur = n;
        while (exist < 10) {
            int tmp = cur;
            while (tmp) {
                int bit = tmp % 10;
                tmp /= 10;
                if (!vis[bit]) {
                     vis[bit] = 1;
                     exist ++;
                }
            }
            cur += n;
        }
        printf("Case #%d: %d\n", kase, cur-n);
    }

    return 0;
}
