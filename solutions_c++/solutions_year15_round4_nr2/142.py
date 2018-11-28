#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); ++e)
typedef long long LL;
typedef pair<double, double> PDD;

int tt, n;
double r[100], c[100];
double v, x;
const double EPS = 1e-9;
bool used[100];
vector<PDD> lo, hi;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        scanf("%d%lf%lf", &n, &v, &x);
        REP(i, n) scanf("%lf%lf", r + i, c + i);
        bool hasMore = false, hasLess = false;
        REP(i, n) if (c[i] > x - EPS)
            hasMore = true;
        REP(i, n) if (c[i] < x + EPS)
            hasLess = true;
        if (!hasMore || !hasLess) {
            printf("Case #%d: IMPOSSIBLE\n", test);
            continue;
        }
        double tot = 0;
        lo.clear();
        hi.clear();
        REP(i, n) {
            bool curMore = c[i] > x - EPS;
            bool curLess = c[i] < x + EPS;
            if (curLess && curMore) {
                tot += r[i];
            } else if (curLess) {
                lo.pb(mp(x - c[i], r[i]));
            } else if (curMore) {
                hi.pb(mp(c[i] - x, r[i]));
            }
        }
        sort(lo.begin(), lo.end(), greater<PDD>());
        sort(hi.begin(), hi.end(), greater<PDD>());
        while (!lo.empty() && !hi.empty()) {
            PDD lob = lo.back();
            PDD hib = hi.back();
            if (lob.first * lob.second > hib.first * hib.second) {
                hi.pop_back();
                tot += hib.second;
                double tmp = (hib.first * hib.second) / lob.first;
                tot += tmp;
                lo.back().second -= tmp;
            } else {
                lo.pop_back();
                tot += lob.second;
                double tmp = (lob.first * lob.second) / hib.first;
                tot += tmp;
                hi.back().second -= tmp;
            }
        }
        assert(tot > EPS);
        printf("Case #%d: %.9f\n", test, v / tot);
    }
	return 0;
}
