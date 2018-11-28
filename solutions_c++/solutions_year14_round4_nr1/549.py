#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int m, n, a[11111];


int main() {

    freopen("bl.in", "r", stdin);
    freopen("bl.out", "w", stdout);

    int T, ca = 0;
    cin >> T;
    while (T--) {
        cin >> n >> m;
        for (int i = 0; i < n; ++i) scanf("%d", a + i);
        sort(a, a + n);
        int l = 0, r = n - 1;
        int cnt = 0;
        while (l <= r) {
            if (l == r) {
                cnt++;
                break;
            }
            if (a[l] + a[r] <= m) {
                l++, r--;
                cnt++;
            } else {
                cnt++;
                r--;
            }
        }
        printf("Case #%d: %d\n", ++ca, cnt);
    }
    return 0;
}
