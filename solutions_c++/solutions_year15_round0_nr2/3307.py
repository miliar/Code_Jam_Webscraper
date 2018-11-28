#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int D, P[1000];
        scanf("%d", &D);
        for (int i = 0; i < D; i++) {
            scanf("%d", P+i);
        }
        int min = 2147483647;
        for (int i = 1; i <= 1000; i++) {
            int op = i;
            for (int j = 0; j < D; j++) {
                if (P[j] > i) {
                    op += (P[j]/i+((P[j]%i != 0)?1:0))-1;
                }
            }
            if (op < min) min = op;
        }
        printf("Case #%d: %d\n", t, min);
    }
    return 0;
}
