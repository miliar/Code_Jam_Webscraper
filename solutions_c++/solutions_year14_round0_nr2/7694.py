#include <iostream>
#include <iomanip>

#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <set>
#include <map>

#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <complex>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; --i)

#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#ifdef SG
    #define debug(x) cerr << #x << ": " << (x) << endl
#else
    #define debug(x)
#endif

template <typename T>
ostream & operator << (ostream & out, vector<T> const & a) {
    out << "[";
    for (int i = 0; i < sz(a); ++i) {
        if (i != 0) {
            out << ", ";
        }
        out << a[i];
    }
    out << "]";
    return out;
}


template <typename T1, typename T2>
ostream & operator << (ostream & out, pair<T1, T2> const & p) {
    out << "(" << p.fs << ", " << p.sc << ")";
    return out;
}

struct Data {
    ld c, f, x;

    bool read () {
        return cin >> c >> f >> x;
    }
    
    ld ans;

    void write () {
        cout.setf(ios::fixed | ios::showpoint);
        cout.precision(10);
        cout << ans << "\n";
    }

    virtual void solve () {}

    virtual void clear () {
        *this = Data();
    }
};


struct Solution: Data {
    bool ok (ld t) {
        int k = 0;
        while (t >= 0) {
            if (t * (2 + f * k) >= x) {
                return true;    
            }
            t -= c / (2 + f * k);
            ++k;
        }
        return false;
    }

    void solve () {
        ld l = 0, r = x / 2;
        static const int ITER_COUNT = 200;
        for (int i = 0; i < ITER_COUNT; ++i) {
            ld m = (l + r) / 2;
            if (ok(m)) {
                r = m;
            }
            else {
                l = m;
            }
        }
        ans = r;
    }

    Solution (Data d = Data()): Data(d) {
    }

    void clear () {
        *this = Solution();
    }
};

Solution sol;

int main () {
#ifdef SG
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        sol.read();
        sol.solve();
        cout << "Case #" << i + 1 << ": ";
        sol.write();
        sol.clear();
    }
#else
    sol.read();
    sol.solve();
    sol.write();    
#endif
    return 0;
}
