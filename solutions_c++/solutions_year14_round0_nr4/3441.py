#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

pair<int, int> solve() {
    int n;
    cin >> n;
    vector<double> a(n), b(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        cin >> b[i];
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    pair<int, int> result;

    int ll = 0, rr = n + 1;
    while (ll + 1 < rr) {
        int mm = ll + ((rr - ll) >> 1);
        bool good = true;
        for (int i = 0; i < mm; ++i)
            if (b[i] > a[n - mm + i]) {
                good = false;
                break;
            }
        if (good)
            ll = mm;
        else
            rr = mm;
    }
    result.first = ll;

    set<double> bb(b.begin(), b.end());
    for (int i = 0; i < n; ++i) {
        set<double>::iterator it = bb.upper_bound(a[i]);
        if (it == bb.end()) {
            bb.erase(bb.begin());
            ++result.second;
        } else {
            bb.erase(it);
        }
    }

    return result;
}

int main() {
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        pair<int, int> ans = solve();
        cout << "Case #" << t << ": " << ans.first << ' ' << ans.second << '\n';
    }

    return 0;
}

