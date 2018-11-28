#include <cstdio>

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", cas);
        for (int i = 1; i <= s; i++)
            printf(" %d", i);
        puts("");
    }
    return 0;
}
