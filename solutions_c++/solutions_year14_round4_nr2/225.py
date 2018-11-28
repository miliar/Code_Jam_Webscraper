#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <array>
#include <map>

using namespace std;

#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

template <typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template <typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template <typename T> inline int sz(const T& x) { return (int) x.size(); }

const double PI = 2 * acos(0);

inline void remove(map<int, int>& m, int x) {
    auto it = m.find(x);
    if (--it->second == 0) {
        m.erase(it);
    }
}

int solve(vector<int>& a) {
    if (sz(a) == 1) {
        return 0;
    }
    int index = min_element(all(a)) - a.begin();
    int d = min(index, sz(a) - 1 - index);
    a.erase(a.begin() + index);
    return solve(a) + d;

}

int main() {
    freopen("B-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    // freopen("in.txt", "r", stdin);

    int nTests;
    cin >> nTests;
    forn (iTest, nTests) {
        cout << "Case #" << iTest + 1 << ": ";
        int n;
        cin >> n;
        vector<int> a(n);
        forn (i, n) {
            cin >> a[i];
        }
        cout << solve(a) << endl;
    }
    return 0;
}