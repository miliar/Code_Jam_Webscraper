#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <ctime>
#include <cstring>
#include <deque>
#include <queue>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
#define MAXN 13
#define MAXD 3
//-----------------------------------------------------------
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int N, R, P, S;
struct C {
	int R, P, S;
	string s;
};

C dp[MAXD][MAXN];
C DP(C win, C lose) {
	C r;
	r.R = win.R + lose.R;
	r.P = win.P + lose.P;
	r.S = win.S + lose.S;
	r.s = (win.s < lose.s) ? (win.s + lose.s) : (lose.s + win.s);
	return r;
}

int main() {

	dp[0][0].P = 1,  dp[0][0].R = 0, dp[0][0].S = 0, dp[0][0].s = "R";
	dp[1][0].P = 0,  dp[1][0].R = 1, dp[1][0].S = 0, dp[1][0].s = "P";
	dp[2][0].P = 0,  dp[2][0].R = 0, dp[2][0].S = 1, dp[2][0].s = "S";
	for (int i = 1; i < MAXN; i++) {
		for (int j = 0;j < MAXD; j++) {
			dp[0][i] = DP(dp[0][i-1], dp[2][i-1]);
			dp[1][i] = DP(dp[1][i-1], dp[0][i-1]);
			dp[2][i] = DP(dp[2][i-1], dp[1][i-1]);
		}
	}

	int cases;
	int casenum = 1;
	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
//		memset(canbe, 0, sizeof(canbe));

		scanf("%d%d%d%d", &N, &R, &P, &S);
		printf("Case #%d: ", casenum++);
		bool isfind = false;
		for (int i = 0; i < MAXD; i++) {
			if (dp[i][N].R != R || dp[i][N].P != P || dp[i][N].S != S) continue;
			printf("%s\n", dp[i][N].s.c_str());
			isfind = true;
			break;
		}
		if (!isfind)
			printf("IMPOSSIBLE\n");
		fflush(stdout);
	}
	return 0;
}

