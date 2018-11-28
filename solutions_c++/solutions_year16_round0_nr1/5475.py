#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef long long ll;

const int INF = 0x3c3c3c3c;

int used[10];

int main() {
    #define task "t"//"eulertour"
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        ll x;
        cin >> x;
        cout << "Case #" << i << ": ";
        if (x) {
            ll ans = x;
            for (ll j = x, cnt = 10; cnt; j += x) {
                ll cur = j;
                while (cur) {
                    int o = cur % 10;
                    cnt -= (used[o] != i);
                    used[o] = i;
                    cur /= 10;
                }
                ans = j;
            }
            cout << ans << endl;
        } else {
            cout << "INSOMNIA" << endl;
        }
    }
    return 0;
}
