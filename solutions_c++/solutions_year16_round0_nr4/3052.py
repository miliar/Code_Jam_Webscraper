#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        long long step = 1;
        for (int i = 1; i < c; ++i) step *= k;
        printf("Case #%d:", cas);
        for (int i = 0; i < s; ++i) {
            printf(" %lld", step * i + 1);
        }
        puts("");
    }
}
