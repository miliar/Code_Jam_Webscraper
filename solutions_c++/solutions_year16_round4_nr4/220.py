#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector < long long > vll;
typedef pair <long long, long long> pll;
typedef pair <int, int> pii;
typedef vector < int > vii;
typedef complex < double > Point;

#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define mp make_pair
#define fst first
#define snd second
#define prev PREV
ll t, n, m, u, v, q, r, ql, qr, k, l, s, w, h, c, z, d, y, x, a;
const int N = 1e5 + 500;
const int K = 1e6 + 500;
const int LN = 20;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 52LL;
const bool JUDGE = false;
string str[N];
int sol;
inline int solve(int fx = 0, int fy = 0) {
    int ret = INT_MAX;
    for (int i = 0; i < n; ++i) {
        if (fx & (1 << i)) continue;
        for (int j = 0; j < n; ++j) {
            if (fy & (1 << j)) continue;
            if (str[i][j] == '1') {
                ret = min(ret, 1 + solve(fx + (1 << i), fy + (1 << j)));
            }
        }
    }
    if (ret == INT_MAX) ret = 0;
    return ret;
}
vector < pii > S;
int main() {
    csl;
    if (JUDGE) {
        freopen("angry.in", "r", stdin);
        freopen("angry.out", "w", stdout);
    }
    cin >> t;
    for (int ii = 1; ii <= t; ++ii) {
        cout << "Case #" << ii << ": ";
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> str[i];
        }
        S.clear();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (str[i][j] == '0') {
                    S.push_back(mp(i, j));
                }
            }
        }
        sol = S.size();
        for (int i = 0; i < (1 << S.size()); ++i) {
            for (int j = 0; j < S.size(); ++j) {
                if (i & (1 << j)) {
                    str[S[j].fst][S[j].snd] = '1';
                }
            }
            if (solve() == n) {
                sol = min(sol, __builtin_popcount(i));
            }
            for (int j = 0; j < S.size(); ++j) {
                if (i & (1 << j)) {
                    str[S[j].fst][S[j].snd] = '0';
                }
            }
        }
        cout << sol << '\n';
    }
    return 0;
}















