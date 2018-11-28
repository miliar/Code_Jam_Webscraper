#include <stdio.h>

int T, t, i, j;
bool was[10];
int K, C, S;
long long KtoC;

int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d: 1", t);
        scanf("%d%d%d", &K, &C, &S);
        KtoC = 1;
        for (i = 0; i < C; i++) {
            KtoC *= K;
        }
        for (i = 1; i < K; i++) {
            printf(" %lld", 1 + i * ((KtoC - 1) / (K - 1)));
        }
        printf("\n");
    }
    return 0;
}
