/*
  Beautiful Codes are MUCH better than 'Shorter' ones !
user  : triveni
date  : 10/04/2016
time  : 00:43:37
*/
#include <bits/stdc++.h>

using namespace std;

#define      pii               std::pair<int,int>
#define      vi                std::vector<int>
#define      mp(a,b)           make_pair(a,b)
#define      pb(a)             push_back(a)
#define      each(it,s)        for(auto it = s.begin(); it != s.end(); ++it)
#define      rep(i, n)         for(int i = 0; i < (n); ++i)
#define      fill(a)           memset(a, 0, sizeof (a))
#define      sortA(v)          sort(v.begin(), v.end())
#define      sortD(v)          sort(v.begin(), v.end(), greater<auto>())
#define      X                 first
#define      Y                 second

typedef long long LL;
LL MOD = 1000000007;

int dp[1<<15];

int solve(int mask, int n) {
	queue<int> Q;
	Q.push(mask);
	dp[mask] = 0;
	while(!Q.empty()) {
		mask = Q.front(); Q.pop();
		for(int i = 1; i <= n; ++i) {
			bitset<32> b = mask;
			for(int j = 0, k = i-1; j <= k; ++j, --k) {
				if(j == k) {
					b[j] = 1 - b[j];
					break;
				}
				bool tmpx = b[j];
				b[j] = 1-b[k];
				b[k] = 1-tmpx;
			}
			int c = b.to_ulong();
			if(dp[c] > dp[mask] + 1) {
				Q.push(c);
				dp[c] = dp[mask] + 1;
			}
			// cerr << c << " " << mask << " " << dp[mask] << "\n";
		}
	}
	return dp[(1<<n)-1];
}

int main()
{
	int T; 
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		printf("Case #%d: ", tc);
		string s; int n;
		cin >> s;
		n = s.length();
		for(int i = 0; i < (1<<n); ++i)
			dp[i] = MOD;
		int num = 0;
		for(int i = 0; i < n; ++i)
			if(s[i]=='+') num |= (1<<i);
		int brute_ans = solve(num, n);
		printf("%d\n",brute_ans);
	}
	return 0;
}
