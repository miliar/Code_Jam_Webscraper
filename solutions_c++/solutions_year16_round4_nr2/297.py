#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define X first
#define Y second
typedef long double ld;

ld dp[205][105];
ld p[205];
ld ip[205];
ld rip[205];

ld find_prob(int n, int k)
{
	dp[0][0] = 1.;
	for (int i = 1; i <= k/2; i++)
	   dp[0][i] = 0.;
	for (int i = 1; i <= k; i++)
	   for (int j = 0; j <= k/2; j++)
	   {
		  
	      dp[i][j] = ip[i-1] * (j==0?0.:dp[i-1][j-1]) + (1. - ip[i-1]) * dp[i-1][j];
	    //  cout << "dp[" << i << "][" << j << "] = " << dp[i][j] << endl;
	   }
	return dp[k][k/2];
}

void solve(int test)
{
	int n,k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) cin >> p[i];
	sort(p, p + n);
	for (int i = 0; i < k/2; i++)
	  ip[i*2] = p[i], ip[i*2+1] = p[n-1-i];
	sort(ip, ip + k);
	//for (int i = 0; i < k; i++) cerr << ip[i] << ' ';
	//cerr << endl;
	ld ans0 = -1;
	for (int t = 0; t <= k; t++)
	{
		for (int i = 0; i < t; i++)
		   ip[i] = p[i];
		for (int i = 0; i < k-t; i++)
		   ip[i+t] = p[n-1-i];
		ans0 = max(ans0, find_prob(n,k));
	}
	/*rip[0] = -1;
	for (int mask = 1; mask < (1<<n); mask++)
	{
		if (__builtin_popcount(mask) != k) continue;
		int cnt = 0;
		for (int i = 0; i < n; i++)
		   if (mask & (1<<i)) ip[cnt++] = p[i];
		assert(cnt == k);
		if (find_prob(n,k) > ans0 ) 
		{
			//sort(ip, ip + k);
			//for (int i = 0; i < k; i++) cerr << ip[i] << ' ';
			//cerr << endl;
			//cout << find_prob(n,k) << ' ' << ans0 << endl;
			//assert(false);
			sort(ip, ip + k);
			for (int i = 0; i < k; i++) rip[i] = ip[i];
			ans0 = find_prob(n,k);
	    }
	}*/
	cout << "Case #" << test << ": " << ans0 << endl;
	//for (int i = 0; i < n; i++) cout << p[i] << ' ';
	//cout << endl;
	//for (int i = 0; i < k; i++) cout << rip[i] << ' ';
	//cout << endl;
}


int main()
{
	int t;
	cin >> t;
	cout.precision(15);
	for (int i = 0; i < t; i++) solve(i+1);
	return 0;
}
