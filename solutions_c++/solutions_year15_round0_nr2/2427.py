#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void solve() {
    int d;
    scanf("%d", &d);
    vector<int> P(d);
    for (int i = 0; i < d; ++i)
        scanf("%d", &P[i]);
    int mx, sp, ans = 1001;
    for (mx = 1; mx <= 1000; ++mx) {
        sp = 0;
        for (int i = 0; i < d; ++i)
            sp += (P[i] - 1) / mx;
        ans = min(ans, sp + mx);
    }
    printf("%d\n", ans);
}

int main() {
    freopen("input.txt", "r", stdin);
    int _T, T;
    scanf("%d", &T);
    for (_T = 1; _T <= T; ++_T) {
        printf("Case #%d: ", _T);
        solve();
    }
    return 0;
}