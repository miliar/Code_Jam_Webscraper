#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef long double ld;
using namespace std;

int main() {
    //ios_base::sync_with_stdio(false)
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        int n = (int)s.size();
        int k;
        cin >> k;
        int ans = 0;
        for(int i = 0; i + k - 1 < n; i++) {
            if(s[i] == '-') {
                ans++;
                for(int j = i; j <= i + k - 1; j++) {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
        bool ok = true;
        for(auto x: s)
            if(x == '-')
                ok = false;
        cout << "Case #" << t << ": ";
        if(!ok)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }
    return 0;
}