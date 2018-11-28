#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>
#include <ctime>
#include <limits>
#include <tuple>
#include <complex>


using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = acos(-1.0l);

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

template<typename T>
void chmin(T &x, T y) {
    x = min(x, y);
}

template<typename T>
void chmax(T &x, T y) {
    x = max(x, y);
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair<U, V> &x) {
    s << "(" << x.fst << ", " << x.snd << ")";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &x) {
    s << "[";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "]";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &x) {
    s << "{";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "}";
    return s;
}

template<int sz>
ostream operator<<(ostream &s, const bitset<sz> &x) {
    for (int i = 0; i < sz; i++) {
        s << x[i];
    }
    return s;
}


//-----------------------------------------------------------------------------



int main() {

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif


    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++) {

        int n;
        cin >> n;

        vector<string> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }


        int m = n * n;
        int ans = 1e9;

        for (int i = 0; i < (1 << m); i++) {
            vector<int> c(n), d(n);
            bool good = true;
            int add = 0;
            for (int j = 0; j < m; j++) {
                if (i & (1 << j)) {
                    c[j / n] |= 1 << (j % n);
                    d[j % n] |= 1 << (j / n);
                    add += a[j / n][j % n] == '0';
                } else {
                    if (a[j / n][j % n] == '1') {
                        good = false;
                    }
                }
            }

            for (int j = 0; j < n; j++) {
                good &= c[j] > 0;
                int x = 0;
                for (int h = 0; h < n; h++) {
                    if (c[j] & (1 << h)) {
                        x |= d[h];
                    }
                }

                if (__builtin_popcount(x) - 1 >= __builtin_popcount(c[j])) {
                    good = false;
                }
            }

            if (good) {
                chmin(ans, add);
            }
        }

        cout << "Case #" << tt << ": " << ans << endl;
    }


    return 0;
}
