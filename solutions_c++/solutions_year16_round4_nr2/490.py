#include <bits/stdc++.h>
using namespace std;

int n, k;
vector <double> prob;
double dp[302];
double nextDP[302];

double calc(vector <double> lis)
{
	/*for(int i = 0; i < lis.size(); i++)
		cout << lis[i] << " ";
	cout << endl;*/
	memset(dp, 0, sizeof(dp));
	dp[0] = 1;
	for(int i = 0; i < lis.size(); i++)
	{
		memset(nextDP, 0, sizeof(nextDP));
		for(int j = 0; j <= lis.size(); j++)
		{
			nextDP[j] += dp[j] * (1.0 - lis[i]);
			nextDP[j+1] += dp[j] * lis[i];
		}
		for(int j = 0; j <= lis.size(); j++)
			dp[j] = nextDP[j];
	}
	return dp[lis.size()/2];
}

bool bad[301];

void solve()
{
	prob.clear();
	cin >> n >> k;
	for(int i = 1; i <= n; i++)
	{
		double t;
		cin >> t;
		prob.push_back(t);
	}
	sort(prob.begin(), prob.end());
	double ans = 0;
	/*for(int mask = 0; mask < (1<<n); mask ++)
	{
		vector <double> u;
		for(int j = 0; j < prob.size(); j++)
			if((mask & (1<<j)) > 0)
				u.push_back(prob[j]);
		if(u.size() == k)
			ans = max(ans, calc(u));
	}*/
	
	for(int i = 0; i+k <= n; i++)
	{
		vector <double> u;
		for(int j = 0; j < k; j++)
			u.push_back(prob[i+j]);
		ans = max(ans, calc(u));
	}


	for(int i = 0; i+(n-k) <= n; i++)
	{
		memset(bad, false, sizeof(bad));
		vector <double> u;
		for(int j = 0; j < n; j++)
			if(j-i < 0 || j-i >= (n-k))
				u.push_back(prob[j]);
		
		ans = max(ans, calc(u));
	}
	

	cout << ans << endl;

}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int ret = MAIN();
	return ret;
}
