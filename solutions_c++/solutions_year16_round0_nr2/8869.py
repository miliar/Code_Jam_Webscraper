#include <bits/stdc++.h>

using namespace std;

#define mem(a, v) memset(a, v, sizeof (a))
#define x first
#define y second
#define all(a) (a).begin(), (a).end()
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
#define rep(i, n) for (int i = 0; i < int(n); i ++)
#define repi(i, a, n) for (int i = (a); i < int(n); i ++)
#define repe(x, v) for (auto x: (v))

int main () {
    std::ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    repi(t, 1, T+1) {
        cout << "Case #" << t << ": ";
        string s;
        cin >> s;
        int ans = 0;
        for (int i = sz(s)-1; i >= 0; i --) {
            if ((ans&1) != (s[i] == '+' ? 0 : 1)) {
                ans ++;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
