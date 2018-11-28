#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define rep2(i,a,b) for (int i=(a);i<(b);i++)
#define rrep(i,n) for (int i=(n)-1;i>=0;i--)
#define rrep2(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define all(a) (a).begin(),(a).end()

typedef long long ll;
typedef pair<int, int> P;
typedef vector<int> vi;
typedef vector<P> vp;
typedef vector<ll> vll;

signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int T;
    cin >> T;

    rep(i, T) {
        string s;
        cin >> s;
        vi a(s.size());
        rep(j, s.size()) {
            a[j] = (s[j] == '+') ? 0 : 1;
        }

        int cnt = 0;
        rep(j, a.size() - 1) {
            if (a[j] != a[j + 1]) {
                cnt++;
            }
        }

        printf("Case #%d: %d\n", i + 1, cnt + (a[0] ^ (cnt & 1)) );
    }
}
