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
        int n, k; scanf("%d%d", &n, &k);
        double p[n]; FOR(i, 0, n) scanf("%lf", p + i);

        double ans = 0.0;
        FOR(b, 0, 1<<n) {
            vi ch; FOR(i, 0, n) if ((1<<i)&b) ch.PB(i); // choose
            if (ch.size() != k) continue;
            double dp[k + 1][k + 1]; CLR(dp); dp[0][0] = 1.0;
            FOR(j, 0, k) {
                FOE(x, 0, j + 1) {
                    int y = j + 1 - x;
                    if (x > 0) dp[x][y] += dp[x - 1][y] * p[ch[j]];
                    if (y > 0) dp[x][y] += dp[x][y - 1] * (1 - p[ch[j]]);
                }
            }
            ans = max(ans, dp[k / 2][k / 2]);
        }

        printf("Case #%d: %.9f\n", ca, ans);
    }
    return 0;
}
