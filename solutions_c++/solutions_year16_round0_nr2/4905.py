#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll getAns(string & s) {
    int ans = 0;
    bool flag = true;

    for (int i = s.size() - 1; i >= 0; --i) {
        if (((s[i] == '-') ^ flag) == false) {
            ++ans;
            flag ^= 1;
        }
    }

    return ans;
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ll t;
    cin >> t;

    for (ll i = 1; i <= t; ++i) {
        string s;
        cin >> s;

        ll ans = getAns(s);
        cout << "Case #" << i << ": " << ans << "\n";
    }

    return 0;
}
