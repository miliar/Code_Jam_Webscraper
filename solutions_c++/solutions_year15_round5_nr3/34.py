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
typedef pair<int, int> PII;

int tt;
int y, n;
int p[25], s[25];
bool c[25];
double pos[25];
double best;
double mul[25];

void go(int v, double me, double curT) {
    if (v == n) {
        best = min(best, curT);
        return;
    }
    int l = -1, r = -1;
    double bestL = 0, bestR = 0;
    REP(i, n) if (!c[i]) {
        if (p[i] < 0) {
            double pp = p[i] - s[i] * curT;
            double t = (me - pp) * mul[i];
            if (l == -1 || t < bestL) {
                l = i;
                bestL = t;
            }
        } else {
            double pp = p[i] + s[i] * curT;
            double t = (pp - me) * mul[i];
            if (r == -1 || t < bestR) {
                r = i;
                bestR = t;
            }
        }
    }
    if (l != -1) {
        c[l] = true;
        go(v + 1, me - y * bestL, curT + bestL);
        c[l] = false;
    }
    if (r != -1) {
        c[r] = true;
        go(v + 1, me + y * bestR, curT + bestR);
        c[r] = false;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        cout << "Case #" << test << ": ";
        cin >> y >> n;
        REP(i, n) cin >> p[i];
        REP(i, n) cin >> s[i];
        REP(i, n) c[i] = false;
        REP(i, n) mul[i] = 1.0 / (y - s[i]);
        best = 1e100;
        go(0, 0, 0);
        cout << setprecision(12) << fixed << best << endl;
    }
	return 0;
}
