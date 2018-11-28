#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define rep2(i,a,b) for (int i=(a);i<(b);i++)
#define rrep(i,n) for (int i=(n)-1;i>=0;i--)
#define rrep2(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define all(a) (a).begin(),(a).end()

typedef long long ll;
typedef pair<int, int> P;


signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int T;
    cin >> T;
    rep(i, T) {
        string s;
        cin >> s;

        string t = "";
        t += s[0];
        rep2(j, 1, s.size()) {
            if (s[j] >= t[0]) {
                t = s[j] + t;
            } else {
                t = t + s[j];
            }
        }

        cout << "Case #" << i + 1 << ": " << t << endl;
    }
}
