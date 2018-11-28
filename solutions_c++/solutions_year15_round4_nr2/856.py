#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define esp 1e-6
#define lson   l, m, rt<<1
#define rson   m+1, r, rt<<1|1
#define sz(x) ((int)((x).size()))
#define pf(x) ((x)*(x))
#define pb push_back
#define pi acos(-1.0)
#define in freopen("OO.in", "r", stdin);
#define IN freopen("solve_in.txt", "r", stdin);
#define out freopen("solve_out.txt", "w", stdout);
#define bug(x) printf("Line : %u >>>>>>\n", (x));
#define TL cerr << "Time elapsed: " << (double)clock() / CLOCKS_PER_SEC * 1000 << " ms" << endl;
#define inf 0x0f0f0f0f
using namespace std;
typedef long long LL;
typedef unsigned US;
typedef pair<int, int> PII;
typedef map<PII, int> MPS;
typedef MPS::iterator IT;


int dblcmp(double x) {
    if (fabs(x) < esp) return 0;
    return x > esp ? 1 : -1;
}
int main () {
//    in
//    out
//    IN
    int T;
    for (int t = scanf("%d", &T); t <= T; t++) {
        int n;
        double V, X;
        scanf("%d%lf%lf", &n, &V, &X);
        bool ok = true;
        double ans = 1e19;
        double R0, R1, C0, C1;
        if (n == 1) {
            scanf("%lf%lf", &R0, &C0);
            if (dblcmp(C0-X) != 0) {
                ok = false;
            } else {
                ans = V/R0;
            }
        } else {
            scanf("%lf%lf%lf%lf", &R0, &C0, &R1, &C1);
            double mi = min(C0, C1);
            double mx = max(C0, C1);
            if (dblcmp(mi-X) > 0 || dblcmp(mx-X) < 0) {
                ok = false;
            } else {
                int r0 = dblcmp(C0-X);
                int r1 = dblcmp(C1-X);
                if (!r0 && !r1) {
                    ans = V/(R0+R1);
                } else if (!r0) {
                    ans = V/R0;
                } else if (!r1) {
                    ans = V/R1;
                } else {
                    double V1 = V*(X-C0)/(C1-C0), V0 = V-V1;
                    ans = max(V1/R1, V0/R0);
                }
            }
        }
        if (!ok) {
            printf("Case #%d: %s\n", t, "IMPOSSIBLE");
        } else
            printf("Case #%d: %.10f\n", t, ans);
    }
    return 0;
}
