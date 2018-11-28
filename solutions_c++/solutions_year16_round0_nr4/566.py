#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    int t;
    cin >> t;
    int cas = 1;
    while (t--) {
        cout << "Case #" << cas << ": ";
        ++cas;
        ll k, c, s;
        cin >> k >> c >> s;
        if (c*s < k) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        ll p = 1;
        ll ant = -1;
        for (int i = 0; i < s; ++i) {
            ll r = p;
            p++;
            p = min(p, k);
            for (int j = 1; j < c; ++j) {
                r = (r - 1)*k;
                r += p;
                p++;
                p = min(p, k);
            }
            if (r == ant) break;
            ant = r;
            if (i) cout << ' ';
            cout << r;
        }
        cout << endl;
    }
}