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

int m, n;
vector<string> S;
VVI A;

int best, res;

void generate(int x) {
    if (x == m) {
        int cost = 0;
        REP(i, n) {
            vector<string> T;
            FORE(j, A[i])
                T.push_back(S[*j]);
            sort(T.begin(), T.end());
            REP(j, SIZE(T)) {
                if (j == 0) {
                    cost += SIZE(T[j]) + 1;
                } else {
                    int k = 0;
                    while (k < SIZE(T[j - 1]) && k < SIZE(T[j]) && T[j - 1][k] == T[j][k])
                        ++k;
                    cost += SIZE(T[j]) - k;
                }
            }
        }
        if (cost == best) {
            ++res;
        } else if (cost > best) {
            best = cost;
            res = 1;
        }
    } else {
        REP(i, n) {
            A[i].push_back(x);
            generate(x + 1);
            A[i].pop_back();
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(ti, 1, t) {
        scanf("%d%d", &m, &n);
        S.clear();
        S.resize(m);
        REP(i, m) {
            char buf[128];
            scanf("%s", buf);
            S[i] = string(buf);
        }

        A.clear();
        A.resize(n);
        best = 0;
        res = 0;
        generate(0);

        printf("Case #%d: %d %d\n", ti, best, res);
    }
}
