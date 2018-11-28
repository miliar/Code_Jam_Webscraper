#include<stdio.h>
#include<string.h>
#include<algorithm>
#define INF 0x3f3f3f3f
int p[1010];
int main() {
    //freopen("input.txt", "rb", stdin);
    freopen("B-large.in", "rb", stdin);
    freopen("output.txt", "wb", stdout);
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt ++) {
        int d, ans = INF;
        scanf("%d", &d);
        for(int i = 0; i < d; i ++) {
            scanf("%d", &p[i]);
        }
        for(int i = 1; i <= 1000; i ++) {
            int n = 0;
            for(int j = 0; j < d; j ++) {
                n += (p[j] - 1) / i;
            }
            ans = std::min(ans, n + i);
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
