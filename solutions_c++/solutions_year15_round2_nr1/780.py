#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

const int N = 1e7 + 100;
int dp[N];

int rev(int x)
{
	int y = 0;
	while (x > 0)
	{
		int d = x % 10;
		y = y * 10 + d;
		x /= 10;
	}
	return y;
}

void preCalc()
{
	dp[1] = 1;
	queue<int> q;
	q.push(1);
	while (q.size() > 0)
	{
		int v = q.front();
		q.pop();

		int u = v + 1;
		if (dp[u] == 0)
		{
			dp[u] = dp[v] + 1;
			q.push(u);
		}
		u = rev(v);
		if (u < N && dp[u] == 0)
		{
			dp[u] = dp[v] + 1;
			q.push(u);
		}
	}
}

void Solution()
{
	int x;
	cin >> x;
	cout << dp[x];
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	preCalc();
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}