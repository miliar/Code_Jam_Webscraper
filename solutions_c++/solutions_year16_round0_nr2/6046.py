#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)

using namespace std;

void solve() {
    string str;
    cin >> str;
    int ans = 0;
    if (str[str.size() - 1] == '-') ans++;
    rep(i, (int)str.size() - 1) {
        if (str[i] != str[i + 1]) ans++;
    }
    cout << ans << endl;
}

int main() {
    int N;
    cin >> N;
    rep(i, N) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
