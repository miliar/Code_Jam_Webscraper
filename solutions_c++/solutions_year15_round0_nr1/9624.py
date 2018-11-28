#include <cstdio>
#include <string.h>
int s[1024];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cases = 0, smax = 0;
    int stand, need;
    char cS;
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        scanf("%d", &smax);
        stand = 0; need = 0;
        for (int j = 0; j <= smax; j++) {
            scanf(" %c", &cS);
            s[j] = cS - '0';
            if (s[j]) {
                if (stand < j) {
                    need += j - stand;
                    stand = j;
                }
                stand += s[j];
            }
        }
        printf("Case #%d: %d\n", i, need);
    }
    return 0;
}
