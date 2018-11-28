// {{{
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <numeric>
#define REP(i, n) for (int i = 0; i < (int) (n); ++i)
#define FOR(i, a, b) for (int i = (int) (a); i <= (int) (b); ++i)
#define FORD(i, a, b) for (int i = (int) (a); i >= (int) (b); --i)
#define FORE(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SIZE(x) ((int) ((x).size()))
#define DEBUG(x) { cerr << #x << ": " << (x) << endl; }
#define SQR(x) ((x) * (x))
#define INF 1023456789
using namespace std;

template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U>& p) {
    os << "(" << p.first << "," << p.second << ")"; return os;
}

template<typename T> ostream& operator << (ostream& os, const vector<T>& v) {
    os << "["; FORE(i, v) { if (i != v.begin()) os << ", "; os << *i; } os << "]"; return os;
}

typedef long long LL;
typedef pair<int, int> PI;
typedef pair<int, PI> TRI;
typedef vector<int> VI;
typedef vector<VI> VVI;
// }}}

double solve() {
    int n, p, q, r, s;
    scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
    VI A(n);
    REP(i, n)
        A[i] = ((LL) i * p + q) % r + s;
    vector<LL> S(n + 1, 0);
    REP(i, n)
        S[i + 1] = S[i] + A[i];

    LL best = S[n];
    REP(i, n) {
        int u = i, v = n;
        while (v - u > 1) {
            int mid = (u + v) / 2;
            if (S[mid] - S[i] < S[n] - S[mid]) {
                u = mid;
            } else {
                v = mid;
            }
        }
        int j = u;
        best = min(best, max(S[i], S[n] - S[j]));
        best = min(best, max(S[i], max(S[j + 1] - S[i], S[n] - S[j + 1])));
    }

    return 1.0 - (double) best / S[n];
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(ti, 1, t) {
        printf("Case #%d: %.10lf\n", ti, solve());
    }
}
