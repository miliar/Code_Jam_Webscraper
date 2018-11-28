#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int n, res = 0, sum = 0;
        cin >> n;
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); j++) {
            int a = s[j] - '0';
            if (a > 0 && sum < j) {
                res += j - sum;
                sum += j - sum;
            }
            sum += a;
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
