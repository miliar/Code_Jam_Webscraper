#include<bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;

    int caseno = 0;
    while (t--) {
        caseno ++;
        int smax;
        cin >> smax;

        string s;
        cin >> s;

        int cnt = 0, ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (cnt < i) {
                ans += (i - cnt);
                cnt += (i - cnt);
            }
            cnt += (s[i] - '0');
        }
        cout << "Case #" << caseno << ": " << ans << endl;
    }

    return 0;
}