#include <bits/stdc++.h>

using namespace std;

int main () {
    ios::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int cs = 0; cs < t; ++cs) {
        int n;
        string s;
        cin >> n >> s;
        int ans = 0;
        for (int i = 0, sum = 0; i <= n; sum += s[i++] - '0') {
            ans = max (ans, i - sum);
        }
        cout << "Case #" << cs + 1 << ": " << ans << endl;
    }

    return 0;
}







