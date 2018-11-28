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

int n;
double v, x;
vector<pair<double, double> > CR;

bool solve(double t) {
    vector<double> L(n);
    REP(i, n)
        L[i] = t * CR[i].second;

    if (n == 1) {
        return v <= L[0];
    } else if (n == 2) {
        double a1 = v * (x - CR[1].first) / (CR[0].first - CR[1].first);
        double a2 = v - a1;
        //cerr << t << " " << L << " " << a1 << " " << a2 << endl;
        return 0 <= a1 && a1 <= L[0] && 0 <= a2 && a2 <= L[1];
    } else {
        return true;
    }
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(ti, 1, t) {
        scanf("%d%lf%lf", &n, &v, &x);
        CR.clear();
        CR.resize(n);
        REP(i, n)
            scanf("%lf%lf", &CR[i].second, &CR[i].first);

        sort(CR.begin(), CR.end());
        REP(i, SIZE(CR) - 1)
            if (CR[i].first == CR[i + 1].first) {
                CR[i].second += CR[i + 1].second;
                CR.erase(CR.begin() + i + 1);
            }
        n = SIZE(CR);

        double min_c = CR[0].first;
        double max_c = CR[n - 1].first;
        if (x < min_c || x > max_c) {
            printf("Case #%d: IMPOSSIBLE\n", ti);
            continue;
        }

        double min_r = INF;
        REP(i, n)
            min_r = min(min_r, CR[i].second);

        double a = 0, b = 2.0 * v / min_r;
        REP(q, 100) {
            double mid = (a + b) / 2;
            if (solve(mid)) {
                b = mid;
            } else {
                a = mid;
            }
        }

        printf("Case #%d: %.9lf\n", ti, b);
    }
}
