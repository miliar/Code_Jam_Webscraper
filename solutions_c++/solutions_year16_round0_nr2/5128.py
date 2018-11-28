#include <bits/stdc++.h>

using namespace std;

#define sz(a) int(a.size())

string s;

int solve() {
    int cnt = 1;
    for (int i = 1; i < sz(s); i++)
        if (s[i] != s[i-1]) cnt++;
    if (s[sz(s) - 1] == '+') cnt--;
    return cnt;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    ios::sync_with_stdio(0);
    int T; cin >> T;
    for (int te = 1; te <= T; te++) {
        cin >> s;
        cout << "Case #" << te << ": " << solve() << endl;
    }
    
    return 0;
}
