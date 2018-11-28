#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define FOREACH(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define MOD 1000000007
#define INF 2000000000

int T, K, N; double p;

const int MAXN = 210;
double dp[MAXN][MAXN];

double getprob(vector<double>& v) {
    FORN(i, MAXN) FORN(j, MAXN) dp[i][j] = 0.0;
    dp[0][0] = 1.0;

    FORN(i, v.size()) {
        FORN(j, MAXN) {
            dp[i+1][j] = dp[i][j] * (1 - v[i]) + dp[i][j-1] * v[i];
        }
    }

    return dp[v.size()][v.size() / 2];
}

int main() {
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        printf("Case #%d: ", tc);

        cin >> N >> K;

        vector<double> vp;
        FORN(i, N) { cin >> p; vp.PB(p); }

        sort(vp.begin(), vp.end());

        double res = 0.0;

        FORN(i, K+1) {
            vector<double> vpk;
            FORN(j, i) vpk.PB(vp[j]);
            FORN(j, K-i) vpk.PB(vp[N-1-j]);
            res = max(res, getprob(vpk));
        }

        cout << setprecision(12) << res << endl;
    }
    
    return 0;
}
