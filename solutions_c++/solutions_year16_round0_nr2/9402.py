#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < (int)(n); ++i)
#define INC(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define DEC(i, a, b) for(int i = (int)(a); i >= (int)(b); --i)
#define CLEAR(a, b) memset(a, b, sizeof a)
#define XX first
#define YY second
#define PB push_back
#define MP make_pair
#define si(a) scanf("%d", &a)
#define sll(a) scanf("%lld", &a)
#define ss(a) scanf("%s", a)

using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;
typedef vector<int> VI;
typedef pair<int, int> II;
typedef vector<II> VII;

const double PI  = acos(-1.0);
const double EPS = 1e-9;
const int INF = 0x3f3f3f3f;
const LL INFL = 0x3f3f3f3f3f3f3f3fLL;

#define LIM 1000
char inp[LIM];
int dp[LIM][2];

int main(void) {
	int tcase; si(tcase);
	REP(_i, tcase) {
		ss(inp);
		CLEAR(dp, 0);
		int len = strlen(inp);

		INC(i, 1, len) {
			if(inp[i-1] == '-') {
				dp[i][1] = min(dp[i-1][1], dp[i-1][0]+2);
				dp[i][0] = min(dp[i-1][1]+1, dp[i-1][0] + 3);
			}
			else if(inp[i-1] == '+') {
				dp[i][0] = min(dp[i-1][0], dp[i-1][1]+2);
				dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]+3);
			}
			else assert(false);
		}

		printf("Case #%d: %d\n", _i+1, dp[len][0]);

	}
}
