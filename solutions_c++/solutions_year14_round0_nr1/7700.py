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

const int N = 4;
struct Item {
    int a[N][N];
    int val;
};

istream & operator >> (istream & in, Item & it) {
    in >> it.val;
    --it.val;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            in >> it.a[i][j];
            --it.a[i][j];
        }
    }

    return in;
}

struct Data {
    Item a, b;    
    bool read () {
        return (cin >> a >> b);
    }
    
    int ans;
    int ansCount;

    void write () {
        if (ansCount == 0) {
            cout << "Volunteer cheated!\n";
        }
        else if (ansCount == 1) {
            cout << ans + 1 << "\n";
        }
        else {
            cout << "Bad magician!\n";
        }
    }

    virtual void solve () {}

    virtual void clear () {
        *this = Data();
    }
};

const int M = N * N;
struct Solution: Data {
    bool can[M];

    void find (Item a, bool can[M]) {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (a.val != i) {
                    can[a.a[i][j]] = false;
                }
            }
        }
    }
         
    void solve () {
        fill(can, can + M, true);
        find(a, can);
        find(b, can);    
        ansCount = 0;
        for (int i = 0; i < M; ++i) {
            if (can[i]) {
                ++ansCount;    
                ans = i;
            }
        }
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
