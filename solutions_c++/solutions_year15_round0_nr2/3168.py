#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn = 1050;
int a[maxn];
int T;
void solve()
{
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
}
int main() {

    freopen("B-large.in", "r", stdin);
    freopen("l_out.txt", "w", stdout);
    solve();

    return 0;
}
