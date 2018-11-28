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


const int MAXN = 242;
ld f[MAXN][MAXN][MAXN];

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
        int n, k;
        cin >> n >> k;
        //memset(f, 0, sizeof(f));
        //f[0][0][0] = 1;
        //for (int i = 0; i < n; ++i) {
            //ld p;
            //cin >> p;
            //for (int j = 0; j <= k; ++j) {
                //for (int t = 0; t <= k / 2; ++t) {
                    //chmax(f[i + 1][j][t], f[i][j][t]);
                    //chmax(f[i + 1][j + 1][t], f[i][j][t] * p);
                    //chmax(f[i + 1][j + 1][t + 1], f[i][j][t] * (1 - p));
                //}
            //}
        //}
        //cout << fixed << f[n][k][k / 2];
        ld p[n];
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
        }
        vector <int> a(n, 0);
        fill(a.begin() + n - k, a.end(), 1);
        ld result = 0;
        do {
            ld f[n + 1];
            memset(f, 0, sizeof(f));
            f[0] = 1;
            for (int i = 0; i < n; ++i) {
                if (a[i]) {
                    for (int j = k / 2; j >= 0; --j) {
                        f[j] = f[j] * p[i];
                        if (j) {
                            f[j] += f[j - 1] * (1 - p[i]);
                        }
                    }
                }
            }
            chmax(result, f[k / 2]);
        } while (next_permutation(a.begin(), a.end()));

        cout.precision(10);
        cout << fixed << result;

        cout << endl;
    }

    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
