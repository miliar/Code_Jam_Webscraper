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

const ld eps = 1e-9;
const int maxn = 205;

ld dp[maxn], ndp[maxn];

int main() {

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif


    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        int n, k;
        cin >> n >> k;

        vector<ld> a;

        for (int i = 0; i < n; i++) {
            ld x;
            cin >> x;
            a.pb(x);
        }

        sort(a.begin(), a.end());

        ld ans = 0.0;
        for (int i = 0; i <= k; i++) {
            vector<ld> b;
            for (int j = 0; j < i; j++) {
                b.pb(a[j]);
            }
            for (int j = 0; j < k - i; j++) {
                b.pb(a[a.size() - 1 - j]);
            }

            fill(dp, dp + maxn, 0);
            dp[0] = 1;
            for (ld x : b) {
                fill(ndp, ndp + maxn, 0);
                for (int j = 0; j + 1 < maxn; j++) {
                    ndp[j + 1] = dp[j + 1] * (1.0 - x) + dp[j] * x;
                }
                ndp[0] = dp[0] * (1.0 - x);
                for (int j = 0; j < maxn; j++) {
                    dp[j] = ndp[j];
                }
            }

            chmax(ans, dp[k / 2]);
        }

        cout.precision(20);
        cout << "Case #" << tt << ": " << fixed << ans << endl;
    }


    return 0;
}
