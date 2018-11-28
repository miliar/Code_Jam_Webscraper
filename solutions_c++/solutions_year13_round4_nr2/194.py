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

typedef long long LL;
typedef pair<int, int> PI;
typedef pair<int, PI> TRI;
typedef vector<int> VI;
typedef vector<VI> VVI;
// }}}

LL solve(LL m, LL p) {
    LL r = 2;
    for (;;) {
        if (p <= m / 2)
            return r - 2;
        p -= m / 2;
        m /= 2;
        r *= 2;
    }
}

int main() {
    int t;
    cin >> t;
    FOR(i, 1, t) {
        int n;
        LL p;
        cin >> n >> p;
        LL m = 1ll << n;
        cout << "Case #" << i << ": ";
        if (p == m) {
            cout << m - 1 << " " << m - 1 << endl;
        } else {
            cout << solve(m, p) << " " << m - 2 - solve(m, m - p) << endl;
        }
    }
}
