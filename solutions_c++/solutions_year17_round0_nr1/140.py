#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        string s;
        int k;
        cin >> s >> k;

        bool flag = true;
        int ans = 0;
        int n = s.length();
        for (int i = 0; i < n; ++ i) {
            if (i + k > n) {
                for (int j = i; j < n; ++ j) if (s[j] == '-') {
                    flag = false;
                    break;
                }
            } else if (s[i] == '-') {
                ++ ans;
                for (int j = 0; j < k; ++ j) {
                    if (s[j + i] == '-') s[j + i] = '+';
                    else s[j + i] = '-';
                }
            }
        }
        cout << "Case #" << t << ": ";
        if (flag) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}
