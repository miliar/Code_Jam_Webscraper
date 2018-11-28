#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <set>
#include <map>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <cstdio>
#include <cassert>
#define repeat(i,n) for (int i = 0; (i) < (n); ++(i))
#define repeat_from(i,m,n) for (int i = (m); (i) < (n); ++(i))
#define repeat_reverse(i,n) for (int i = (n)-1; (i) >= 0; --(i))
#define repeat_from_reverse(i,m,n) for (int i = (n)-1; (i) >= (m); --(i))
#define dump(x)  cerr << #x << " = " << (x) << endl
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl
typedef long long ll;
template <class T> bool setmax(T & l, T const & r) { if (not (l < r)) return false; l = r; return true; }
template <class T> bool setmin(T & l, T const & r) { if (not (r < l)) return false; l = r; return true; }
using namespace std;
template <class T> ostream & operator , (ostream & out, T a) { return out << a; }
#define endl "\n"
template <class T>
using reversed_priority_queue = priority_queue<T, vector<T>, greater<T> >;
template <class T> istream & operator >> (istream & in, vector<T> & a) { for (T & it : a) in >> it; return in; }
template <class T> ostream & operator << (ostream & out, vector<T> const & a) { bool i = false; for (T const & it : a) { if (i) out << ' '; else i = true; out << it; } return out; }
void solve() {
    int n, k; cin >> n >> k;
    vector<double> p(n); repeat (i,n) cin >> p[i];
    sort(p.begin(), p.end());
    vector<vector<vector<double> > > cur(k+1);
    vector<vector<vector<double> > > prv; {
        vector<double> f(n+1);
        f[0] = 1;
        cur[0].push_back(f);
    }
    repeat (i,n) {
        prv = cur;
        repeat (j,min(i+1,k)) {
            for (auto && f : prv[j]) {
                vector<double> g(n+1);
                repeat (l,j+1+1) {
                    if (l-1 >= 0) g[l] += f[l-1] * p[i];
                    g[l] += f[l] * (1 - p[i]);
                }
                cur[j+1].push_back(g);
            }
            sort(cur[j+1].rbegin(), cur[j+1].rend(), [&](vector<double> const & f, vector<double> const & g) {
                return f[(j+2)/2] + f[(j+1)/2] < g[(j+2)/2] + g[(j+1)/2];
            });
            // const double eps = 0.01;
            // auto it = find_if(cur[j+1].begin(), cur[j+1].end(), [&](vector<double> const & f) {
            //     return f[(j+2)/2] + f[(j+1)/2] + eps < cur[j+1][0][(j+2)/2] + cur[j+1][0][(j+1)/2];
            // });
            // assert (it != cur[j+1].begin());
            // cur[j+1].erase(it, cur[j+1].end());
        }
    }
    cout << cur[k][0][k/2] << endl;
cerr << cur[k][0][k/2] << endl;
}
int main() {
    int t; cin >> t;
    repeat (i,t) {
cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
