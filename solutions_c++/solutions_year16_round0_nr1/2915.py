#include <cstdio>
#include <cstring>

char tmp[25];

int main() {
    freopen("A.in", "rt", stdin);
    freopen("A.out", "wt", stdout);
    int t, n, mask;

    scanf("%d", &t);

    for (int tc = 1, i; tc <= t; tc++) {
        scanf("%d", &n);
        mask = 0;
        for (i = 1; i <= 100 && mask != (1<<10)-1; i++) {
            sprintf(tmp, "%d", i * n);
            for (int j = 0; j < strlen(tmp); j++)
                mask |= (1 << (tmp[j] - '0'));
        }
        if (mask == (1 << 10)-1)
            printf("Case #%d: %d\n", tc, (i-1) * n);
        else
            printf("Case #%d: INSOMNIA\n", tc);
    }

    return 0;
}
