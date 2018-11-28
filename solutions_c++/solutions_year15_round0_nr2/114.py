#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int N, M;
int main(){
    int T, i, ca;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int D, P[1005];
        scanf("%d", &D);
        for (int i = 0; i < D; ++i) {
            scanf("%d", &P[i]);
        }
        int mint = 10000;
        for (int k = 1; k <= 1000; ++k) {
            int t = k;
            for (int i = 0; i < D; ++i)
                t += ((P[i] - 1) / k + 1) - 1;
            if (t < mint)
                mint = t;
        }
        printf("Case #%d: %d\n", ca, mint);
    }
    return 0;
}
