#include<stdio.h>
#include<string.h>
char s[1010];
int main() {
    //freopen("input.txt", "rb", stdin);
    freopen("A-large.in", "rb", stdin);
    freopen("output.txt", "wb", stdout);
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt ++) {
        int sum, ans, m;
        sum = ans = 0;
        scanf("%d%s", &m, s);
        for(int i = 0; i <= m; i ++) {
            if(sum < i) {
                ans += i - sum;
                sum = i;
            }
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
