#include <bits/stdc++.h>

using namespace std;

void solve() {
    string s;
    cin >> s;
    vector < char > a;
    a.clear(); a.push_back(s[0]);
    for (int i = 1; i < s.size(); i++) {
        if (s[i] != s[i - 1])
            a.push_back(s[i]);
    }
    int ans = 0;
    for (int i = 1; i < a.size(); i++) {
        ans++;
    }
    if (a.back() == '-')
        ans++;
    cout << ans << endl;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test = 0;
    cin >> test;
    for (int id = 1; id <= test; id++){
        cout << "Case #" << id << ": ";
        solve();
    }
    return 0;
}