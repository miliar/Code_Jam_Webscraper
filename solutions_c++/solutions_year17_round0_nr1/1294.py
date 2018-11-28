#include <bits/stdc++.h>
using namespace std;

// IOI 2018

int t, k;
string s;

int main() {
    freopen("A_in.txt", "r", stdin);
    freopen("A_out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> t;
    for (int T = 1; T <= t; ++T) {
        cin >> s >> k;
        int cnt = 0;
        bool ok = 1;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '-') {
                if (i + k - 1 >= s.size()) {
                    ok = 0; break;
                }
                for (int j = i; j <= i + k - 1; ++j) {
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
                cnt++;
            }
        }
        cout << "Case #" << T << ": ";
        if (!ok) {
            cout << "IMPOSSIBLE\n";
        }
        else cout << cnt << '\n';
    }
}
