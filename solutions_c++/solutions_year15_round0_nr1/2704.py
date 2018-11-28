// LUCIFER <3 SLS <3

#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out-large.txt", "w", stdout);
    int t, k, i, ans, cnt, u = 0;
    string s;
    cin >> t;
    while (t--) {
        cin >> k >> s;
        ans = 0;
        cnt = 0;
        for (i = 0; i <= k; i++) {
            if (cnt < i && s[i] != '0') {
                ans += (i-cnt);
                cnt = i;
            }
            cnt += (s[i]-48);
        }
        cout << "Case #" << ++u << ": " << ans << endl;
    }
    return 0;
}
