#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

const double EPS = 1e-9;
const double INF = 1e30;

double fle(double x, double y) { return x < y + EPS; }
double feq(double x, double y) { return fabs(x-y) < EPS; }

int N;
double V, X;
double R[10000], C[10000];

int main() {
    int T; scanf("%d", &T); FOE(ca, 1, T) {
        scanf("%d%lf%lf", &N, &V, &X);
        FOR(i, 0, N) scanf("%lf%lf", R + i, C + i);

        // Small
        double ans = INF;
        if (N == 1) {
            if (feq(C[0], X))
                ans = V / R[0];

        } else {
            if (feq(C[0], C[1])) {
                if (feq(X, C[0])) {
                    ans = V / (R[0] + R[1]);
                }
            } else {
                double alp = (X - C[1]) / (C[0] - C[1]);
                if (fle(0, alp) && fle(alp, 1)) {
                    ans = max(alp * V / R[0], (1 - alp) * V / R[1]);
                }
            }
        }

        printf("Case #%d: ", ca);
        if (ans == INF) puts("IMPOSSIBLE");
        else printf("%.9f\n", ans);
    }
    return 0;
}
