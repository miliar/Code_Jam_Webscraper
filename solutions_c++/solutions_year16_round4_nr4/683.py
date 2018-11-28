#include <iostream>
#include <cstdio>
#include <cassert>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#ifdef LOCAL
#define dbg(x) cerr << #x " = " << x << endl;
#include "pretty_print.h"
#else
#define dbg(x)
#endif

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;

#define snd second
#define fst first

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0? -x : x; }
template <typename T> T gcd(T a, T b) { return b? gcd(b, a % b) : a; }
template <typename T> bool chmin(T &x, const T& y) { if (x > y) { x = y; return true; } return false; }
template <typename T> bool chmax(T &x, const T& y) { if (x < y) { x = y; return true; } return false; }

bool check(vector <string> a, int n, vector <int> s) {
    vector <int> m;
    m.push_back(0);

    for (int i = 0; i < n; ++i) {
        vector <int> b;
        for (auto j : m) {
            bool ok = false;
            for (int k = 0; k < n; ++k) {
                if (a[s[i]][k] == '1' && (!(j & (1 << k)))) {
                    ok = true;
                    b.push_back(j | (1 << k));
                }
            }

            if (!ok) {
                return false;
            }
        }
        m = b;
        sort(m.begin(), m.end());
        m.resize(unique(m.begin(), m.end()) - m.begin());
    }

    return true;
}

bool check(vector <string> a, int n) {
    vector <int> s(n);
    for (int i = 0; i < n; ++i) {
        s[i] = i;
    }

    do {
        if (!check(a, n, s)) {
            return false;
        }
    } while (next_permutation(s.begin(), s.end()));
    return true;
}

int main(int /* argc */, char** /* argv */)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifdef LOCAL
    assert(freopen("inp", "r", stdin));
    assert(freopen("out", "w", stdout));
    #endif
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        int n;
        cin >> n;
        vector <string> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        int answer = n * n;
        for (int m = 0; m < (1 << n * n); ++m) {
            auto b = a;
            int x = m;
            int c = 0;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (x & 1) {
                        b[i][j] = '1';
                        c += a[i][j] == '0';
                    }
                    x >>= 1;
                }
            }
            if (c >= answer) {
                continue;
            }

            if (check(b, n)) {
                answer = c;
            }
        }
        cout << answer;
        cout << endl;
    }

    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
