#include <cstdio>
#include <cstring>

int a[1010], l[1010], r[1010];
int min(int a, int b) {
    return a < b ? a : b;
}

void work() {
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i ++)
        scanf("%d", a + i);
    memset(l, 0, sizeof(l));
    memset(r, 0, sizeof(r));
    for(int i = 1; i <= n; i ++) {
        for(int j = 1; j <= i; j ++)
            if(a[j] > a[i]) l[i] ++;
        for(int j = i; j <= n; j ++)
            if(a[i] < a[j]) r[i] ++;
    }
    int ans = 0;
    for(int i = 1; i <= n; i ++)
        ans += min(l[i], r[i]);
    printf("%d\n", ans);
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++)
        printf("Case #%d: ", i), work();
    return 0;
}
