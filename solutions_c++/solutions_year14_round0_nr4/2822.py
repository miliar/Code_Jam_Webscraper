#include <iostream>
#include <set>

using namespace std;

const int MAXN = 1005;
long double wa[MAXN], wb[MAXN];
set<long double> a, b;

int main() {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tt = 0; tt < t; tt++) {
        int n;
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >> wa[i];
            a.insert(wa[i]);
        }
        for(int i = 0; i < n; i++) {
            cin >> wb[i];
            b.insert(wb[i]);
        }
        int ans = 0;
        for(int i = 0; i < n; i++) {
            set<long double>::iterator it = a.lower_bound(*b.begin());
            if(it == a.end()) {
                a.erase(a.begin());
                set<long double>::iterator it = b.end();
                it--;
                b.erase(it);
            }
            else {
                a.erase(it);
                b.erase(b.begin());
                ans++;
            }
        }
        for(int i = 0; i < n; i++)
            b.insert(wb[i]);
        int ans0 = 0;
        for(int i = 0; i < n; i++) {
            set<long double>::iterator it = b.lower_bound(wa[i]);
            if(it == b.end()) {
                b.erase(b.begin());
                ans0++;
            }
            else
                b.erase(it);
        }
        cout << "Case #" << tt + 1 << ": " << ans << ' ' << ans0 << '\n';
    }
    return 0;
}
