#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int cal(int x) {
    if (!x) return 0;
    int vis[10];
    memset(vis, 0, sizeof(vis));
    int tmp = x, cur = 0;
    for ( ; tmp; tmp /= 10) {
        if (vis[tmp % 10]) continue;
        vis[tmp % 10] = 1;
        cur++;
    }
    for (int mul = 2; ; ++mul) {
        int data = mul * x;
        for ( ; data; data /= 10) {
            if (vis[data % 10]) continue;
            vis[data % 10] = 1;
            if (++cur == 10) return mul;
        }
    }
}
int main() {
    int T, cas = 0; scanf("%d", &T);
    while (T-- > 0) {
        int n; scanf("%d", &n);
        if (!n) printf("Case #%d: INSOMNIA\n", ++cas);
        else printf("Case #%d: %d\n", ++cas, cal(n) * n);
    }
    return 0;
}
