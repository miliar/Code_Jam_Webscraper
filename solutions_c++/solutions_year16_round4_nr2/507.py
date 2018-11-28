#include<bits/stdc++.h>
#define rep(i,k,n) for(int i= (int) k;i< (int) n;i++)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;
const int limit = 1048576;
using namespace std;

// checklist
// long longi
// treść źle przeczytana
// przypadki brzegowe(min max wejście)

int main()
{
    ios_base::sync_with_stdio(0);
//     cin.tie(0);
    int T; cin >> T;
    rep(t, 1, T + 1) {
        int n, k; cin >> n >> k;
        vector<ld>p(n);
        for(auto& l : p)
            cin >> l;
        sort(all(p));
        ld res = 0;
        rep(i, 0, k + 1) {
            vector<ld> comittee;
            rep(j, 0, i)
                comittee.pb(p[j]);
            rep(j, n - (k - i), n)
                comittee.pb(p[j]);
//             for(auto p : comittee)
//                 cout << p << " ";
//             cout << "\n";
            vector<vector<ld> >dp(k + 1, vector<ld>(k + 1, 0.0));
            dp[0][0] = 1.0;
            rep(j, 1, k + 1)
                rep(l, 0, j + 1) {
                    if(l > 0)
                        dp[j][l] += comittee[j - 1] * dp[j - 1][l - 1];
                    if(l < j)
                        dp[j][l] += (1 - comittee[j - 1]) * dp[j - 1][l];
//                     cout << j << " " << l << " " << dp[j][l] << "\n";
                }
            res = max(res, dp[k][k / 2]);
//             cout << "\n";
        }
        cout << setprecision(10) << fixed << "Case #" << t << ": " << res << "\n";
    }
    return 0;
}