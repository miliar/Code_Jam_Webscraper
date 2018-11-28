#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

main () {
    freopen ("d.in", "r", stdin);
    freopen ("d.out", "w", stdout);
    int t;
    cin >> t;
    int tc = 1;
    while (t--) {
        int n;
        cin >> n;
        set <long double> a, b, la, lb;
        for (int i = 0; i < n; ++i) {
            long double x;
            cin >> x;
            a.insert(x);
        }
        for (int i = 0; i < n; ++i) {
            long double x;
            cin >> x;
            b.insert(x);
        }
        la = a;
        lb = b;
        int ans = 0, res = 0;
        for (int i = 0; i < n; ++i) {
            long double x = *a.rbegin ();
            set <long double> :: iterator it = b.upper_bound(x);
            if (it == b.end ()) it = b.begin ();
            if (x > *it) ++res;
            b.erase(it);
            a.erase(x);
        }
        a = la;
        b = lb;
        for (int i = 0; i < n; ++i) {
            long double x = *b.begin ();
            set <long double> :: iterator it = a.upper_bound(x);
            if (it == a.end ()) it = a.begin ();
            if (x < *it) ++ans;
            a.erase(it);
            b.erase(x);
        }
        cout << "Case #" << tc << ": " << ans << " " << res << "\n";
        ++tc;
    }
}
