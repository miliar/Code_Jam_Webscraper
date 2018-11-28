#include <bits/stdc++.h>

using namespace std;

int t;

int main() {
    freopen("B.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    iostream::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> t;
    for (int r = 0; r < t; r++) {
        string s;
        cin >> s;
        cout << "Case #" << r + 1 << ": ";
        int cnt = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] != s[i - 1]) {
                cnt++;
            }
        }
        if (s[s.size() - 1] == '-') {
            cnt++;
        }
        cout << cnt << "\n";
    }
}
