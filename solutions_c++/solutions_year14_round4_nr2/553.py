#include <iostream>
#include <cstdio>

using namespace std;
int a[1111], ok[1111];
const int inf = 1000000009;
int main() {

    freopen("bl.in", "r", stdin);
    freopen("bl.out", "w", stdout);

    int T, ca = 0;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        for (int i = 1; i <= n; ++i)
            cin >> a[i];
        for (int i = 1; i <= n; ++i) ok[i] = true;
        int ans = 0;
        for (int k = 1; k <= n; ++k) {
            int cnt = 0;
            int pos = 0, mi = inf, id = 0;;
            for (int i = 1; i <= n; ++i) {
                if (!ok[i]) continue;
                cnt++;
                if (a[i] < mi) {
                    mi = a[i];
                    pos = cnt;
                    id = i;
                }
            }
            int l = pos - 1;
            int r = cnt - pos;
            ok[id] = false;
            ans = ans + min(l, r);
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}
