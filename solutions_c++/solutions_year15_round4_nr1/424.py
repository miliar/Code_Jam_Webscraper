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

int r, c;
vector<vector<char> > A;

char dc[4] = {'^', '>', 'v', '<'};
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

bool safe(int x, int y, int d) {
    for (;;) {
        x += dx[d];
        y += dy[d];
        if (x < 0 || y < 0 || x >= c || y >= r)
            return false;
        if (A[y][x] != '.')
            return true;
    }
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(ti, 1, t) {
        scanf("%d%d", &r, &c);
        A.clear();
        A.resize(r, vector<char>(c));
        REP(i, r) REP(j, c)
            scanf(" %c", &A[i][j]);

        int res = 0;
        bool possible = true;
        REP(i, r) REP(j, c) if (A[i][j] != '.') {
            if (!possible)
                break;
            int d = -1;
            REP(k, 4) if (A[i][j] == dc[k])
                d = k;
            assert(d != -1);
            if (!safe(j, i, d)) {
                bool ok = false;
                REP(k, 4) if (k != d && safe(j, i, k)) {
                    ok = true;
                    break;
                }
                if (ok) {
                    ++res;
                } else {
                    possible = false;
                    break;
                }
            }
        }

        if (possible) {
            printf("Case #%d: %d\n", ti, res);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", ti);
        }
    }
}
