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
#include <climits>
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
    int n; cin >> n;
    vector<vector<int> > a(2*n-1, vector<int>(n));
    repeat (i,2*n-1) repeat (j,n) cin >> a[i][j];
    vector<vector<int> > b(n, vector<int>(n, -1));
    vector<int> used(2*n-1, -1);
    int missing = -1;
    function<bool (int)> rec = [&](int i) {
        if (i == n) return true;
        int min_a = INT_MAX;
        vector<int> js;
        repeat (j,2*n-1) if (used[j] == -1) {
            if (setmin(min_a, a[j][i])) js.clear();
            if (min_a == a[j][i]) js.push_back(j);
        }
        assert (1 <= js.size() and js.size() <= 2);
        if (js.size() == 1) missing = i;
        for (int j : js) used[j] = i;
        vector<vector<int> > saved_b = b;
        {
            bool valid = true;
            repeat (k,n) {
                if (b[i][k] == -1) {
                    b[i][k] = a[js[0]][k];
                } else {
                    if (b[i][k] != a[js[0]][k]) {
                        valid = false;
                        break;
                    }
                }
            }
            if (js.size() == 2) {
                repeat (k,n) {
                    if (b[k][i] == -1) {
                        b[k][i] = a[js[1]][k];
                    } else {
                        if (b[k][i] != a[js[1]][k]) {
                            valid = false;
                            break;
                        }
                    }
                }
            }
            if (valid) {
                if (rec(i+1)) return true;
            }
        }
        b = saved_b;
        {
            bool valid = true;
            repeat (k,n) {
                if (b[k][i] == -1) {
                    b[k][i] = a[js[0]][k];
                } else {
                    if (b[k][i] != a[js[0]][k]) {
                        valid = false;
                        break;
                    }
                }
            }
            if (js.size() == 2) {
                repeat (k,n) {
                    if (b[i][k] == -1) {
                        b[i][k] = a[js[1]][k];
                    } else {
                        if (b[i][k] != a[js[1]][k]) {
                            valid = false;
                            break;
                        }
                    }
                }
            }
            if (valid) {
                if (rec(i+1)) return true;
            }
        }
        b = saved_b;
        for (int j : js) used[j] = -1;
        return false;
    };
    bool result = rec(0);
    assert (result);
    assert (missing != -1);
    vector<int> x(n); repeat (i,n) x[i] = b[i][missing];
    vector<int> y(n); repeat (i,n) y[i] = b[missing][i];
    vector<int> ans = count(a.begin(), a.end(), x) ? y : x;
    cout << ans << endl;
}
int main() {
    int t; cin >> t;
    repeat (i,t) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
