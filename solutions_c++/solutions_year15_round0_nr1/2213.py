#include <cstdio>
int main() {
    int n;
    scanf("%d", &n);
    for (int k = 0; k < n; ++k) {
        int m, sum = 0, ans = 0;
        scanf("%d ", &m);
        for (int i = 0; i <= m; ++i) {
            char c;
            scanf("%c", &c);
            int diff = i - sum;
            if (diff > 0) {
                ans += diff;
                sum += diff;
            }
            sum += c - '0';
        }
        printf("Case #%d: %d\n", k + 1, ans);
    }
}
