#include <bits/stdc++.h>
#define int long long
using namespace std;


signed main()
{
	int t; cin >> t;
	for (int tc=1; tc<=t; tc++) {
	int dp[101]={};
	string x; cin >> x;
	for (int i=x.length(); i>=1; i--)
		if (x[i-1]=='-') dp[i] = dp[i+1]&1 ? dp[i+1] : dp[i+1]+1;
		else dp[i] = dp[i+1]&1 ? dp[i+1]+1 : dp[i+1];
	cout << "Case #" << tc << ": " << dp[1] << endl;
	}
}
