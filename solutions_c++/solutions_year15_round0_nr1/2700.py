#include <bits/stdc++.h>
using namespace std;

void solve() {
    int smax;
    cin >> smax;
    string s_str;
    cin >> s_str;
    int res = 0;
    int lower = 0;
    for(int i = 0; i <= smax; ++i) {
        int s = s_str[i] - '0';
        if(s == 0) continue;
        if(lower < i) {
            res += i - lower;
            lower += i - lower;
            lower += s;
        } else {
            lower += s;
        }
        // cout << "i = " << i << ", s = " << s << ", res = " << res << ", lower = " << lower << endl;
    }
    cout << res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cout.precision(30);

    int T;
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
