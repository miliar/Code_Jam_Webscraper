// Author: thecodekaiser
#include <bits/stdc++.h>
using namespace std;

#define INF 1000000007
#define MXN 1005

int dp[MXN][MXN];
int arr[MXN];

void setval(int & num, int ret)
{
	if(num == -1)
		num = ret;
	else
		num = min(ret, num);
	return;
}

void solve(int CS)
{
	memset(dp, -1, sizeof(dp));
	int D;
	scanf("%d", &D);
	
	int mx = 0;
	for(int i = 0; i < D; i++)
		scanf("%d", &arr[i]), mx = max(arr[i], mx);
		
	dp[0][0] = 0;	
	
	for(int i = 0; i < D; i++)
	{
		for(int j = 0; j < mx; j++)
		{
			if(dp[i][j] == -1)	continue;
			
			setval(dp[i+1][j], max(dp[i][j], arr[i]));
			
			for(int k = 2; k * k <= arr[i] and k + j < mx; k++)
			{
				int ex = (arr[i] / k) + ((arr[i] % k == 0) ? 0 : 1);
				
				setval(dp[i+1][j+k-1], max(ex, dp[i][j]));
			}
		}
	}
	
	int ans = INF;
	for(int i = 0; i < mx; i++)
		if(dp[D][i] != -1)
			ans = min(ans, dp[D][i] + i);
		
	printf("Case #%d: %d\n", CS, ans);
	
	return;
}

int main()
{
	int t, CS = 1;
	cin >> t;
	
	while(t--)
		solve(CS++);
	return 0;
}
