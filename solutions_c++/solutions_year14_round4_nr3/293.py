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

int w, h;

inline int encode_in(int i, int j) {
    return 2 * (i * w + j);
}

inline int encode_out(int i, int j) {
    return 2 * (i * w + j) + 1;
}

inline int decode_row(int x) {
    return x / 2 / w;
}

VVI G;
vector<bool> V;

bool DFS(int x) {
    V[x] = true;
    if (decode_row(x) == h - 1)
        return true;
    FORE(i, G[x]) if (!V[*i] && DFS(*i)) {
        G[*i].push_back(x);
        G[x].erase(i);
        return true;
    }
    return false;
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(ti, 1, t) {
        int n;
        scanf("%d%d%d", &w, &h, &n);
//        if (ti == 3)
//            cerr << w << " " << h << " " << n << endl;
        VI X0(n), Y0(n), X1(n), Y1(n);
        map<int, int> M;
        h += 2;
        REP(i, n) {
            scanf("%d%d%d%d", &X0[i], &Y0[i], &X1[i], &Y1[i]);
//            if (ti == 3)
//                cerr << X0[i] << " " << Y0[i] << " " << X1[i] << " " << Y1[i] << endl;
            ++X1[i];
            ++Y1[i];

            ++Y0[i];
            ++Y1[i];

            M[Y0[i]] = 0;
            M[Y1[i]] = 0;
        }
//        h = 1;
//        FORE(i, M)
//            i->second = h++;
//        REP(i, n) {
//            Y0[i] = M[Y0[i]];
//            Y1[i] = M[Y1[i]];
//        }
        vector<vector<bool> > A(h, vector<bool>(w, true));
        REP(i, n) FOR(y, Y0[i], Y1[i] - 1) FOR(x, X0[i], X1[i] - 1)
            A[y][x] = false;

        G.clear();
        G.resize(2 * w * h);
        int di[4] = {0, 1, 0, -1};
        int dj[4] = {1, 0, -1, 0};
        REP(i, h) REP(j, w) if (A[i][j]) {
            G[encode_in(i, j)].push_back(encode_out(i, j));
            REP(d, 4) {
                int ni = i + di[d];
                int nj = j + dj[d];
                if (0 <= ni && ni < h && 0 <= nj && nj < w && A[ni][nj])
                    G[encode_out(i, j)].push_back(encode_in(ni, nj));
            }
        }

        int res = 0;
        REP(i, w) {
            V.clear();
            V.resize(2 * w * h, false);
            res += DFS(encode_in(0, i));
        }
        printf("Case #%d: %d\n", ti, res);
    }
}
