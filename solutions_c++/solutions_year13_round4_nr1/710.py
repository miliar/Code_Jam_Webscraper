#include <algorithm>
#include <iostream>
#include <climits>
#include <list>
#include <map>
#include <cmath>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <numeric>

using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)  

const long long MOD = 1000002013;
int N, M;
long long s[1000], t[1000], p[1000];

long long dist(long long x, long long y, long long n, long long p) {
    long long d = y - x;
    long long ret = d * (n + n - d + 1) / 2;
    ret %= MOD;
    return ret * p % MOD;
}

long long dp[2048][2048];

void solve() {
    cin >> N >> M;

    long long ret = 0;
    REP (i, M) {
        cin >> s[i] >> t[i] >> p[i];
        --s[i];
        --t[i];
        ret += dist(s[i], t[i], N, p[i]);
        ret %= MOD;
    }

    vector<long long> x;
    REP (i, M) {
        x.push_back(s[i]);
        x.push_back(t[i]);
    }
    sort(x.begin(), x.end());
    x.erase(unique(x.begin(), x.end()), x.end());

    memset(dp, 0, sizeof(dp));
    ret = (MOD - ret) % MOD;
    REP (k, x.size()) {
        // take on
        REP (i, M) {
            if (s[i] == x[k])
                dp[k][k] += p[i];
        }
        // take off
        long long cnt = 0;
        REP (i, M) {
            if (t[i] == x[k])
                cnt += p[i];
        }

        for (int i = 2048; i >= 0; i--) {
            if (dp[k][i] == 0)
                continue;
            if (cnt >= dp[k][i]) {
                cnt -= dp[k][i];
                ret += dist(x[i], x[k], N, dp[k][i]);
                ret %= MOD;
                dp[k][i] = 0;
            }
            else {
                dp[k][i] -= cnt;
                ret += dist(x[i], x[k], N, cnt);
                ret %= MOD;
                cnt = 0;
            }
        }

        REP (i, 2048)
            dp[k+1][i] = dp[k][i];
    }

    ret = (MOD - ret) % MOD;
    cout << ret << endl;
}


int main() {
    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << (i+1) << endl;
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
    return 0;
}
