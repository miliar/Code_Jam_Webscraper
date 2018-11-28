#include <cstdio>

int main() {
    int t;
    scanf("%d", &t);

    for (int cs = 1; cs <= t; ++cs) {
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d:", cs);
        for (int i = 1; i <= k; ++i) {
            printf(" %d", i);
        }
        printf("\n");
    }
}
