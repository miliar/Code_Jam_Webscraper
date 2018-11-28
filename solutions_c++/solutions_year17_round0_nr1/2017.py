#include <bits/stdc++.h>

using namespace std;

string s;

void change(int l, int r) {
    for (int i = l; i <= r; ++i)
        if (s[i]=='+') s[i] = '-';
        else s[i] = '+';
}

void solve() {
    int k;
    cin >> s >> k;
    cin.ignore();
    int n = s.length(), res = 0;
    for (int i = k-1; i < n; ++i) {
        if (s[i-k+1] == '-') {
            change(i-k+1,i);
            ++res;
        }
    }
    int cnt = 0;
    for (int i = 0; i < n; ++i)
        cnt += (s[i]=='+');
    if (cnt!=n) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t; cin >> t; int te = t; cin.ignore();
    while (t--) {
        cout << "Case #" << te-t << ": ";
        solve();
    }
	return 0;
}
