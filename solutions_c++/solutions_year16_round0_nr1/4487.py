#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll solve(ll n) {
    if (n == 0)
        return -1;

    int flag = 0;
    for (ll i = 1; ; i++) {
        // cout << n * i << endl;

        ll temp = n * i;
        if (i < 0) {
            cout << "overflow\n";
            return -2;
        }

        while (temp > 0) {
            int digit = temp % 10;
            temp /= 10;

            flag |= (1 << digit);
        }

        if (flag == (1 << 10) - 1)
            return n * i;
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int TC; cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        cout << "Case #" << tc << ": ";
        ll inp; cin >> inp;
        ll ans = solve(inp);
        if (ans == -1) cout << "INSOMNIA" << "\n";
        else cout << ans << "\n";
    }

    return 0;
}
