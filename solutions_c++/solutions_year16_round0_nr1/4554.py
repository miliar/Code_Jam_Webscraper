#include <cstdiO>
#include <algorithm>
#include <string.h>
#include <vector>
#include <iostream>
using namespace std;
typedef long long LL;
const LL inf = 0x3f3f3f3f3f3f3f3f;
int n, T, tt = 0, m;
bool vis[10];
LL solve(LL k) {
    int num = 0;
    LL i = 1, sum = k;
    memset(vis, 0, sizeof vis);
    if (k == 0) return -1;
    while (k < inf) {
        LL d = k;
        while (d) {
            if (vis[d % 10] == false) ++num;
            vis[d % 10] = true;
            d /= 10;
        }
        if (num == 10) return k;
        ++i;
        k = sum * i;
    }
    return -1;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    while (T--) {
        cin >> m;
        LL ans = solve(m);
        if (ans == -1) cout << "Case #" << ++tt << ": INSOMNIA\n";
        else cout << "Case #" << ++tt << ": " << ans << "\n";
    }
    return 0;
}
