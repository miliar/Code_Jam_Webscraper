#include <stdio.h>
char c[1010];
int main(){
    int T, ri = 1, n, i, cnt, ans, x;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d%s", &n, c);
        cnt = ans = 0;
        for (i = 0; i <= n; i++) {
            x = c[i] - '0';
            if (x && cnt < i) {
                ans += i - cnt;
                cnt = i;
            }
            cnt += x;
        }
        printf("Case #%d: %d\n", ri++, ans);
    }
    return 0;
}
