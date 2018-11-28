
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

const string BAD = "IMPOSSIBLE";

string solve(int n, int p, int r, int s) {
    if (n == 0) {
        if (r) return "R";
        if (p) return "P";
        if (s) return "S";
    }

    int a = p + r - s;
    int b = p + s - r;
    int c = r + s - p;

    if (a%2 || b%2 || c%2) return BAD;
    if (min({a,b,c}) < 0) return BAD;

    a /= 2; b /= 2; c /= 2;

    string sol = solve(n-1, a, b, c);
    if (sol == BAD) return BAD;

    string ans;
    for (char c : sol) {
        if (c == 'P') ans += "PR";
        if (c == 'R') ans += "PS";
        if (c == 'S') ans += "RS";
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    FOR(i,1,t) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;

        cout << "Case #" << i << ": " << solve(n, p, r, s) << '\n';
    }

    return 0;
}

/*************************************************************************/

