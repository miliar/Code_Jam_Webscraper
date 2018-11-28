#include <bits/stdc++.h>

using namespace std;


inline void solve(int test) {

    int n, x;
    cin >> n >> x;
    int a[n];
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int ans = 0;
    multiset<int, greater<int> > s;
    for (int i = 0; i < n; ++i) {
        s.insert(a[i]);
    }
    while (!s.empty()) {
        ++ans;
        int sz1 = *s.begin();
        s.erase(s.begin());
        auto it = s.lower_bound(x - sz1);
        if (it != s.end()) {
            s.erase(it);
        }
    }

    cout << "Case #" << test << ": " << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }

    return 0;
}
