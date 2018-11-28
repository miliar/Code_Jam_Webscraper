#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        string s;
        cin >> s;
        int ans = 0;
        for (int i = 0; i < (int)s.size() - 1; ++i) {
            if (s[i] != s[i + 1])
                ++ans;
        }
        if (s.back() == '-')
            ++ans;
        cout << "Case #" << i + 1 << ": " << ans << '\n';
    }
    return 0;
}
