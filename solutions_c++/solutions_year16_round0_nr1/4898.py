#include <stdio.h>

int T, t, i, j;
bool was[10];
long long n, k;

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%lld", &n);
        if (n == 0) printf("INSOMNIA\n");
        else {
            for (i = 0; i < 10; i++) was[i] = false;
            k = n;
            for (n = k;; n += k) {
                j = n;
                while (j > 0) {
                    was[j % 10] = true;
                    j /= 10;
                }
                for (i = 0; i < 10; i++) j += was[i];
                if (j == 10) {
                    printf("%lld\n", n);
                    break;
                }

            }
        }
    }
    return 0;
}
