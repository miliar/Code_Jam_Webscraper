#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())
#define	endl			'\n'

typedef long long		ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>		vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>		vpii;

const int MX = 101;

int dp[MX][2];

const int MOD = 1000000007;

int solve(string &s)
{
	int n = s.length();
	int k = n-1;
	while (k >= 0 && s[k] == '+') --k;
	if (k < 0) return 0;
	if (n == 1) return 1;
	++k;
	if (s[0] == '-') {
		dp[0][0] = 0;
		dp[0][1] = 1;
	} else {
		dp[0][0] = 1;
		dp[0][1] = 0;
	}
	FOR(i,1,k) {
		if (s[i] == '+') {
			dp[i][1] = min(dp[i-1][1],dp[i-1][0]+1);
			dp[i][0] = min(dp[i-1][1]+1,dp[i-1][0]+2);
		} else {
			dp[i][0] = min(dp[i-1][0],dp[i-1][1]+1);
			dp[i][1] = min(dp[i-1][1]+2,dp[i-1][0]+1);
		}
	}
	return min(dp[k-1][1],dp[k-1][0]+1);
}

int main(int argc, char *argv[])
{
#ifndef ONLINE_JUDGE
	freopen(argv[1],"r",stdin);
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	ios :: sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;
	string s;
	FOR(testcase,1,T+1) {
		cin >> s;
		int res = solve(s);
		cout << "Case #" << testcase << ": " << res << endl;
	}
	return 0;
}
