#include <stdio.h>
#include <string.h>

void solve(int n) {
    if (n == 0) {
        printf("INSOMNIA\n");
        return;
    }
    int d[10];
    memset(d, 0, sizeof(d));
    int cnt0 = 10;
    int cur_n = 0;
    while (cnt0 > 0) {
        cur_n += n;
        int v = cur_n;
        while (v) {
            cnt0 -= d[v % 10] == 0;
            d[v % 10] = 1;
            v /= 10;
        }
    }
    printf("%d\n", cur_n);
}
int main() {
    int T, n;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d", &n);
        printf("Case #%d: ", i + 1);
        solve(n);
    }
    return 0;
}
    
