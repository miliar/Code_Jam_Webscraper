#include <cstdio>

int main() {
    int T, N;

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        int marked = 0, n = 0;
        while (marked != 1023) {
            n += N;
            int x = n;
            while (x) {
                marked |= 1<<(x%10);
                x /= 10;
            }
        }
        printf("Case #%d: %d\n", t, n);
    }
}
