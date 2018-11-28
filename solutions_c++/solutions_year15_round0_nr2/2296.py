#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int maxn = 1100;
int d[maxn], f[maxn], g[maxn];
int n;

void init() {

}

int main() {
    init();
    int tt; cin >> tt;
    int cas = 0;
    while (tt--) {
        int ans = 0;
        int mx = 0;
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d", d + i), mx = max(mx, d[i]);
        ans = mx;
        
        for (int i = 1; i <= mx; ++i) {
            int tot = i;
            for (int j = 1; j <= n; ++j)
                if (d[j] > i) {
                    if (d[j] % i == 0)
                        tot += (d[j] / i - 1);
                    else
                        tot += d[j] / i;
                }
            ans = min(ans, tot);
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

