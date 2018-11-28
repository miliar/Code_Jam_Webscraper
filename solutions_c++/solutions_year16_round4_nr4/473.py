
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

bool check(int n, vector <vector<bool>> &can) {
    int N = (1 << n);

    bool dp[N][N];
    FOR(i,0,N-1) FOR(j,0,N-1) {
        dp[i][j] = (j == 0);
    }

    FOR(i,0,N-1) FOR(j,1,N-1) {
        int bit = __builtin_ctz(j);
        int rest = (j ^ (1 << bit));

        FOR(left,0,n-1) if (i & (1 << left)) {
            int sub = (i ^ (1 << left));

            dp[i][j] |= dp[sub][j];
            dp[i][j] |= (can[left][bit] && dp[sub][rest]);

            if (dp[i][j]) break;
        }
    }

    FOR(i,0,n-1) {
        int neigh = 0;
        FOR(j,0,n-1) if (can[i][j]) {
            neigh |= (1 << j);
        }

        int rest = (N-1) ^ (1 << i);
        if (dp[rest][neigh]) return false;
    }

    return true;
}

int solve(int n, vector <vector<bool>> &can) {
    int m = n * n;
    int M = (1 << m);

    int smallest = m;
    FOR(mask,0,M-1) {
        int s = __builtin_popcount(mask);
        if (s >= smallest) continue;

        vector <vector<bool>> changed = can;

        bool redundant = false;
        FOR(i,0,m-1) if (mask & (1 << i)) {
            int a = i / n, b = i % n;
            if (can[a][b]) redundant = true;

            changed[a][b] = 1;
        }

        if (!redundant && check(n, changed)) smallest = s;
    }

    return smallest;
}

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    FOR(i,1,t) {
        int n;
        cin >> n;

        vector <vector<bool>> can(n, vector <bool> (n));
        FOR(a,0,n-1) FOR(b,0,n-1) {
            char c; cin >> c;
            can[a][b] = (c == '1');
        }

        cout << "Case #" << i << ": " << solve(n, can) << '\n';
    }

    return 0;
}

/*************************************************************************/

