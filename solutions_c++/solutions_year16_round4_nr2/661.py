
#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define SIZE(c) (int) (c).size()
#define FORE(i,c) FOR(i,0,SIZE(c)-1)
#define FORDE(i,c) FORD(i,SIZE(c)-1,0)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

using namespace std;

typedef long long int LLI;
typedef pair < int , int > PII;
typedef pair < LLI , LLI > PLL;

typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < PII > VP;
typedef vector < LLI > VL;
typedef vector < PLL > VPL;

typedef vector < VI > VVI;
typedef vector < VL > VVL;
typedef vector < VB > VVB;
typedef vector < VP > VVP;

const int MOD = 1000000007;
const int INF = 1000000001;
const LLI LLINF = 1000000000000000001LL;

/*************************************************************************/

double score(vector <double> &p) {
    int n = SIZE(p);
    int k = n / 2;

    double dp[n+1][k+1];

    dp[0][0] = 1.0;
    FOR(j,1,k) dp[0][j] = 0.0;

    FOR(i,1,n) FOR(j,0,k) {
        double x = p[i-1];
        dp[i][j] = dp[i-1][j] * (1.0 - x) + (j ? dp[i-1][j-1] * x : 0.0);
    }

    return dp[n][k];
}

double solve(int n, int k, vector <double> &p) {
    int N = (1 << n);

    double ans = 0.0;
    FOR(mask,0,N-1) if (__builtin_popcount(mask) == k) {
        vector <double> sub;
        FOR(i,0,n-1) if (mask & (1 << i)) {
            sub.PB(p[i]);
        }

        ans = max(ans, score(sub));
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    cout << setprecision(9) << fixed;

    int t;
    cin >> t;

    FOR(i,1,t) {
        int n, k;
        cin >> n >> k;

        vector <double> p(n);
        FOR(j,0,n-1) cin >> p[j];

        cout << "Case #" << i << ": " << solve(n, k, p) << '\n';
    }

    return 0;
}

/*************************************************************************/

