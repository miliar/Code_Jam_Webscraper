#include <iostream>
using namespace std;
int main () {
    ios::sync_with_stdio(0);
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        int k, n, ans = 0;
        cin >> s >> k;
        n = s.length();
        for (int i = 0; i <= n - k; i ++)
            if (s[i] == '-') {
                ans ++;
                for (int j = i; j < i + k; j ++)
                    s[j] = (s[j] == '-' ? '+' : '-');
            }
        for (int i = 0; i < n; i ++)
            if (s[i] != '+')
                ans = -1;
        cout << "Case #" << t << ": ";
        if (ans >= 0)
            cout << ans;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }
}
