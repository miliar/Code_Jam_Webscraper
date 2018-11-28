#include <bits/stdc++.h>
using namespace std;

void solve() {
    int r, c, w;
    cin >> r >> c >> w;

    int ans = (r - 1) * (c / w);
    ans += (c - (c % w == 0)) / w;
    ans += w;
    cout << ans << "\n";
}

int main() {

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
