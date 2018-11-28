#include <bits/stdc++.h>

#define fi first
#define se second
#define ll long long
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

#define maxn 1000009

using namespace std;

int t, n, dp[maxn];

queue <int> q;

int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	
	scanf("%d", &t);
	
	fill(dp, dp+maxn, maxn);
	
	q.push(1);
	
	dp[1] = 1;
	
	while (!q.empty())
	{
		int k = q.front();
		
		q.pop();
		
		int a = k+1, b = 0, k1 = k;
		
		while (k)
			b = b*10+k%10, k/=10;
		
		if (a < 1000001 && dp[a] > dp[k1]+1)
			dp[a] = dp[k1]+1, q.push(a);
		
		if (b < 1000001 && dp[b] > dp[k1]+1)
			dp[b] = dp[k1]+1, q.push(b);
	}
	
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		printf("Case #%d: %d\n", i, dp[n]);
	}
}

