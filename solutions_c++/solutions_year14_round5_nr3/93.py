#include <bits/stdc++.h>

using namespace std;

#define long int64_t

#define rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=a;i<(b);++i)
#define all(u) begin(u),end(u)
#define rall(u) (u).rbegin(),(u).rend()
#define uniq(u) (u).erase(unique(all(u)),end(u))

#define mp make_pair
#define pb push_back
#define eb emplace_back

const int N = 1024;
const int M = 2048;

int n, id[N];
char info[N];

int m, zip[M], unzip[M];

void input()
{
    vector<int> v;

    cin >> n;
    rep(i, n) {
        cin >> info[i] >> id[i];
        if (id[i]) v.pb(id[i]);
    }
    sort(all(v));
    uniq(v);

    m = v.size();
    rep(i, m) {
        zip[v[i]] = i;
        unzip[i] = v[i];
    }
}


int solve()
{
    vector<pair<int, int> > p;
    rep(i, 1 << m) rep(j, n + 1) p.pb(mp(i, j));
    rep(i, n) {
        vector<pair<int, int> > np;
        if (info[i] == 'E') {
            if (id[i] == 0) {
                for (pair<int, int>& e : p) {
                    np.pb(mp(e.first, e.second + 1));
                    rep(j, m) if (~e.first >> j & 1) {
                        np.pb(mp(e.first | 1 << j, e.second));
                    }
                }
            } else {
                for (pair<int, int>& e : p) {
                    const int& z = zip[id[i]];
                    if (~e.first >> z & 1) {
                        np.pb(mp(e.first | 1 << z, e.second));
                    }
                }
            }
        } else if (info[i] == 'L') {
            if (id[i] == 0) {
                for (pair<int, int>& e : p) {
                    if (e.second >= 1) np.pb(mp(e.first, e.second - 1));
                    rep(j, m) if (e.first >> j & 1) {
                        np.pb(mp(e.first ^ 1 << j, e.second));
                    }
                }
            } else {
                for (pair<int, int>& e : p) {
                    const int& z = zip[id[i]];
                    if (e.first >> z & 1) {
                        np.pb(mp(e.first ^ 1 << z, e.second));
                    }
                }
            }
        }
        p = np;
    }
    if (p.empty()) return -1;

    int ans = n;
    for (pair<int, int>& e : p) {
        ans = min(ans, __builtin_popcount(e.first) + e.second);
    }
    return ans;
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    rep(i, T) {
        input();

        cout << "Case #" << i + 1 << ": ";
        int ans = solve();
        if (ans >= 0) cout << ans << endl;
        else cout << "CRIME TIME" << endl;
    }

    return 0;
}
