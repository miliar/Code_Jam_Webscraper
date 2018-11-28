
#include <stdio.h>

int main() {
    int T;
    int Smax;
    char n;
    int total;
    int adicionado;
    int c;
    int i;
    scanf("%d", &T);
    for (c = 1; c <= T; c++) {
        total = 0;
        adicionado = 0;
        scanf("%d ", &Smax);
        Smax++;
        for (i = 0; i < Smax; i++) {
            scanf("%c", &n);
            n = n - '0';
            if (total < i) {
                adicionado += i - total;
                total = i;
            }
            total += n;
        }
        printf("Case #%d: %d\n", c, adicionado);
    }
    return 0;
}
