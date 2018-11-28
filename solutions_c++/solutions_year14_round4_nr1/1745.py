#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, c;
        cin >> n >> c;
        int a[n];
        multiset <int> s;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            s.insert(a[i]);
        }
        sort (a, a + n);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (!s.count (a[i])) continue;
            auto it = s.upper_bound (c - a[i]);
            auto q = s.lower_bound (a[i]);
            ++ans;
            if (it == s.begin ()) {
                s.erase (q);
                continue;
            }
            --it;
            if (q == it) {
                if (it == s.begin ()) {
                    s.erase (q);
                    continue;
                }
                --it;
            }
            s.erase (q);
            s.erase (it);
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
}
