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

int p, q, n;
VI H, G;

map<TRI, int> memo;

int f(int skipped, int first_monster, int hp_taken) {
    if (first_monster == n)
        return 0;

    TRI key = TRI(first_monster, PI(hp_taken, skipped));
    if (memo.count(key))
        return memo[key];

    int res = 0;
    if (H[first_monster] - hp_taken <= q) {
        res = max(res, f(skipped + 1, first_monster + 1, 0));
    } else {
        res = max(res, f(skipped + 1, first_monster, hp_taken + q));
    }
    if (H[first_monster] - hp_taken <= skipped * p) {
        int steps = (H[first_monster] - hp_taken + p - 1) / p;
        res = max(res, f(skipped - steps, first_monster + 1, 0) + G[first_monster]);
    }

    return memo[key] = res;
}

int solve() {
    scanf("%d%d%d", &p, &q, &n);
    H.clear();
    H.resize(n);
    G.clear();
    G.resize(n);
    REP(i, n)
        scanf("%d%d", &H[i], &G[i]);
    memo.clear();
    return f(1, 0, 0);
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(ti, 1, t) {
        printf("Case #%d: %d\n", ti, solve());
    }
}
