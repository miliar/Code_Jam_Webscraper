#include <cstdio>

const int ALL = (1 << 10) - 1;

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", cas);
        if (n > 0) {
            int ans = 0;
            int flag = 0;
            for (ans = 1; flag != ALL; ans++) {
                int cur = ans * n;
                for (; cur > 0; cur /= 10)
                    flag |= (1 << (cur % 10));
            }
            printf("%d\n", (ans - 1) * n);
        } else printf("INSOMNIA\n");
    }
    return 0;
}

