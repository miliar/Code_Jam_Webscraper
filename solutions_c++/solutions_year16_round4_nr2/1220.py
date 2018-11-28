#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
#define pb push_back
#define MAXN 20
using namespace std;

vector <double> v;
double dp[MAXN][MAXN];
int used[MAXN][MAXN];
int m;

double p[MAXN];

double solve2(int pos, int need) {
    if (pos >= m) {
        if (need == 0) {
            return 1;
        }
        return 0;
    }
    if (used[pos][need]) {
        return dp[pos][need];
    }

    double aux = v[pos] * solve2(pos + 1, need - 1) + (1 - v[pos]) * solve2(pos + 1, need);
    used[pos][need] = 1;
    dp[pos][need] = aux;
    return aux;
}

double solve(void) {
    memset(used, 0, sizeof(used));
    return solve2(0, m / 2);
}

int main(void) {
    int t;
    int n, k;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        scanf(" %d %d", &n, &k);
        for (int i = 0; i < n; i++) {
            scanf(" %lf", &p[i]);
        }

        double res = 0;
        for (int mask = 0; mask < 1 << n; mask++) {
            v.clear();
            for (int i = 0; i < n; i++) {
                int bit = (mask >> i) & 1;
                if (bit) {
                    v.pb(p[i]);
                }
            }

            m = (int)v.size();
            if (m == k) {
                res = max(res, solve());
            }
        }
        printf("Case #%d: %.12f\n", caso, res);
    }
    return 0;
}
