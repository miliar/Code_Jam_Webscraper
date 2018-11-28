#include <bits/stdc++.h>
using namespace std;

double arr[200];
double arr2[200];
double dp[201][201];
int n,k;

double rec(int pos, int curr)
{
	if(curr==k)
	{
		dp[k][0] = 1;
		for(int i=1; i<=k/2; i++)
			dp[k][i] = 0;

		for(int i=k-1; i>=0; i--)
		{
			for(int j=min(k-i,k/2); j>=0; j--)
			{
				int x = k-i-j;
				dp[i][j] = 0;
				if(j)
					dp[i][j] += dp[i+1][j-1]*arr2[i];
				if(x)
					dp[i][j] += dp[i+1][j]*(1.00-arr2[i]);
			}
		}

		return dp[0][k/2];
	}
	if(pos==n)
		return 0;

	arr2[curr] = arr[pos];
	return max(rec(pos+1,curr),rec(pos+1,curr+1));
}

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		cin >> n >> k;
		for(int i=0; i<n; i++)
			cin >> arr[i];

		cout << "Case #" << cn << ": " << fixed << setprecision(7) << rec(0,0) << endl;
	}

	return 0;
}