#include <stdio.h>

bool nisp[33333334];
int p[2100000];
int np = 0;
int T, t, n, jj;
int i, j, m, bit;
long long val[11], k;
int div[11];

int main() {
    for (i = 2; i < 33333334; i++) {
        if (nisp[i]) continue;
        p[np++] = i;
        for (j = i + i; j < 33333334; j += i) nisp[j] = true;
    }
    fprintf(stderr, "%d\n", np);
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d:\n", t);
        scanf("%d%d", &n, &jj);
        for (m = 0; jj > 0 && m < (1 << (n - 2)); m++) {
            for (i = 2; i <= 10; i++) val[i] = 1;
            for (bit = 0; bit < n - 2; bit++) {
                for (i = 2; i <= 10; i++) val[i] = i * val[i] + !!(m & (1 << bit));
            }
            for (i = 2; i <= 10; i++) val[i] = i * val[i] + 1;
            for (i = 2; i <= 10; i++) {
                div[i] = 0;
                for (j = 0; ((long long)p[j])*p[j] <= val[i]; j++) {
                    if (val[i] % p[j] == 0) {
                        div[i] = p[j];
                        break;
                    }
                }
                if (div[i] == 0) break;
            }
            if (i > 10) {
                jj--;
                printf("%lld", val[10]);
                for (i = 2; i <= 10; i++) printf(" %d", div[i]);
                printf("\n");
            }
        }
    }
    return 0;
}
