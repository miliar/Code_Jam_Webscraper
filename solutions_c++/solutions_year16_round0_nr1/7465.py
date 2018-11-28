#include <stdio.h>
long long int solve (long long N) {
    long long int i;
    long long int s;
    int len = 10;
    int a[10] = {};
    int j;
    if (N == 0) {
        return -1;
    }
    for (i = 1;; i++) {
        s = (N*i);
        while (1) {
            a[s % 10] = 1;
            s /= 10;
            if (s == 0) break;
        }
        for (j = 0; j <= 9; j++) {
            if (a[j] == 0) break;
            if (j == 9) return N*i;
        }
    }    
}
int main (void) {
    long long T, i;
    long long ans;
    long long N;
    scanf("%lld", &T);
    for (i = 1; i <= T; i++) {
        scanf("%lld", &N);
        ans = solve(N);
        if (ans == -1) {
            printf("Case #%lld: INSOMNIA\n", i);
        }
        else {
            printf("Case #%lld: %lld\n", i, ans);
        }
    }
    return 0;
}
