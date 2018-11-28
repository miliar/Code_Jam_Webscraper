#include <bits/stdc++.h>
using namespace std;

#define ALL(a) a.begin(), a.end()
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORE(i,c) for (int i = 0; i < int((c).size()); ++i)
#define MEM(a,v) memset((a), (v), sizeof(a))
#define SZ(a) int(a.size())
#define pb push_back
#define mp make_pair
#define ft first
#define sd second

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = (1 << 30);
const int MOD = 1000000007;
const double EPS = 1e-7;

int main() {
    //ios_base::sync_with_stdio(false); cin.tie(0);
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        double ans = X / 2;
        double tt = 0, pr = 2;
        //printf("Farms=0, time=%.7lf\n", ans);
        //int nf = 0;
        while (true) {
            tt += C / pr;
            pr += F;
            double ntime = tt + X / pr;
            //++nf;
            //printf("Farms=%d, time=%.7lf\n", nf, ans);
            if (ntime < ans + EPS) {
                ans = ntime;
            }
            else break;
        }
        printf("Case #%d: %.7lf\n", tc, ans);
    }
    return 0;
}