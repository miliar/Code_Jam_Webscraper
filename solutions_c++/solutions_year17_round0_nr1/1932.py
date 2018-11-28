#include <bits/stdc++.h>

using namespace std;

int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        string s;
        int k;
        cin >> s >> k;

        int ans = 0;

        for (int i = 0; i + k <= s.length(); ++i) {
            if (s[i] == '-') {
                ++ans;
                for (int j = i; j < i + k; ++j) {
                    s[j] = (s[j] == '+') ? '-' : '+';
                }
            }
        }

        cout << "Case #" << t << ": ";
        if (any_of(s.begin(), s.end(), [](char c){ return c == '-';}))
            cout << "IMPOSSIBLE";
        else
            cout << ans;
        cout << '\n';
    }

    return 0;
}
