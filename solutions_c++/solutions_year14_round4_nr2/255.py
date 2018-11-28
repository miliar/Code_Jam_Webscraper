#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1);

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

const int N = 2000;

int dp[2][N];
int at[N];

int Less[N];

const int INF = 0x3F3F3F3F;

void solve(int nowCase) {
	int n;
	cin >> n;
	vector<int> s(n);
	REP(i, n) cin >> s[i];
	vector<int> t = s;
	SORT(t);
	REP(i, n) s[i] = lower_bound(ALL(t), s[i]) - t.begin();

	REP(i, n) at[s[i]] = i;
	REP(i, n) Less[i] = 0;
	REP(i, n) REP(j, i) if (s[j] > s[i]) ++Less[i];

	REP(i, n + 1) dp[0][i] = INF;
	dp[0][0] = 0;
	REP(i, n) {
		int now = i & 1, next = now ^ 1;
		REP(j, n + 1) dp[next][j] = INF;
		REP(j, n + 1) {
			if (dp[now][j] == INF) continue;
			{
				dp[next][j + 1] = min(dp[next][j + 1], dp[now][j] + Less[at[i]]);
			}
			{
				dp[next][j] = min(dp[next][j], dp[now][j] + n - i - Less[at[i]] - 1);
			}
		}
	}

	int ans = INF;
	REP(j, n + 1) {
		ans = min(ans, dp[n & 1][j]);
	}

	//assert(ans % 2 == 0);

	cout << "Case #" << nowCase << ": " << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int nowCase = 1; nowCase <= T; ++nowCase) {
		solve(nowCase);
	}
	return 0;
}