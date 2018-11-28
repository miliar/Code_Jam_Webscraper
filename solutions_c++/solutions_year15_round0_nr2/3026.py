#include<bits/stdc++.h>
#define in freopen("B-large.in", "r", stdin);
#define out freopen("solve_out.txt", "w", stdout);
using namespace std;
const int maxn = 1111;
int a[maxn];
int main() {

    in
    out
    int T;
    for (int t = scanf("%d", &T); t <= T; t++) {
        int  n;
        scanf("%d", &n);
        int mx = 0;
        for (int i = 1; i <= n; i++) {
            scanf("%d", &a[i]);
            mx = max(mx, a[i]);
        }
        int ans = mx;
        for (int i = 1; i <= mx; i++) {
            int tmp = 0;
            for (int j = 1; j <= n; j++) {
                tmp += (a[j] + i - 1) / i - 1;
            }
            ans = min(ans, tmp + i);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
