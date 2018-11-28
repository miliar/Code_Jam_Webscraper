#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

void solve() {
    int smax;
    string s;
    cin >> smax >> s;

    int ans = 0;
    int count = 0;
    rep(i, smax + 1) {
        if (count >= i) {
            count += s[i] - '0';
        } else {
            ans++;
            count += s[i] - '0' + 1;
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": "; 
        solve();
    }
    return 0;
}
