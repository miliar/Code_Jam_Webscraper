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
        vector<bool> E(n);
        VI W(n);
        REP(i, n) {
            char c;
            scanf(" %c %d", &c, &W[i]);
            E[i] = (c == 'E');
        }

        VI P;
        REP(i, n) if (W[i] != 0)
            P.push_back(W[i]);
        sort(P.begin(), P.end());
        P.resize(distance(P.begin(), unique(P.begin(), P.end())));
        int p = SIZE(P);
        int u = 2 * n + 1;

        REP(i, n) {
            if (W[i] == 0) {
                W[i] = -1;
            } else {
                REP(j, p) if (P[j] == W[i]) {
                    W[i] = j;
                    break;
                }
            }
        }

        vector<vector<bool> > D(1 << p, vector<bool>(u, true));
        REP(i, n) {
            vector<vector<bool> > T(1 << p, vector<bool>(u, false));
            REP(x, 1 << p) REP(j, u) if (D[x][j]) {
                if (E[i]) {
                    if (W[i] == -1) {
                        if (j + 1 < u)
                            T[x][j + 1] = true;
                        REP(k, p) if ((x & (1 << k)) == 0)
                            T[x | (1 << k)][j] = true;
                    } else {
                        if ((x & (1 << W[i])) == 0)
                            T[x | (1 << W[i])][j] = true;
                    }
                } else {
                    if (W[i] == -1) {
                        if (j - 1 >= 0)
                            T[x][j - 1] = true;
                        REP(k, p) if ((x & (1 << k)) != 0)
                            T[x &~ (1 << k)][j] = true;
                    } else {
                        if ((x & (1 << W[i])) != 0)
                            T[x &~ (1 << W[i])][j] = true;
                    }
                }
            }
            D.swap(T);
        }

        int res = INF;
        REP(x, 1 << p) REP(j, u) if (D[x][j]) {
            int cnt = 0;
            REP(k, p)
                if ((x & (1 << k)) != 0)
                    ++cnt;
            res = min(res, cnt + j);
        }

        printf("Case #%d: ", ti);
        if (res == INF) {
            printf("CRIME TIME\n");
        } else {
            printf("%d\n", res);
        }
    }
}
