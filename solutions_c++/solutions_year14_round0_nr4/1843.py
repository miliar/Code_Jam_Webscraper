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

int main() {
    int t;
    scanf("%d", &t);
    FOR(ti, 1, t) {
        int n;
        scanf("%d", &n);
        vector<double> A(n);
        REP(i, n)
            scanf("%lf", &A[i]);
        sort(A.begin(), A.end());
        vector<double> B(n);
        REP(i, n)
            scanf("%lf", &B[i]);
        sort(B.begin(), B.end());

        int res_war = n;
        for (int i = n - 1, j = n - 1; i >= 0; --i)
            if (A[i] < B[j]) {
                --res_war;
                --j;
            }

        VVI D(n + 1, VI(n + 1, 0));
        FOR(el, 1, n) REP(i, n) {
            int j = i + el;
            if (j > n)
                continue;
            if (A[n - el] < B[j - 1])
                D[i][j] = max(D[i][j], D[i][j - 1]);
            if (A[n - el] > B[i])
                D[i][j] = max(D[i][j], 1 + D[i + 1][j]);
        }

        printf("Case #%d: %d %d\n", ti, D[0][n], res_war);
    }
}
