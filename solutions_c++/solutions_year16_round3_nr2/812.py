#include <iostream>
#include <cstdio>

using namespace std;

long long N, K;
bool way[55][55];
int mmm[9];
long long ans;
int IN[9];

void dfs(int v)
{
	IN[v] = 1;
	for (int i = 1; i <= N; i++)
	{
		if (ans == -1)
		{
			return;
		}
		if (way[v][i])
		{
			if (IN[i] == 1)
			{
				ans = -1;
				return;
			}
			if (IN[i] == 0)
				dfs(i);
		}
	}
	IN[v] = 2;
	return;
}

long long dp[55];

void print()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (way[i][j])
				cout << "1";
			else
				cout << "0";
		}
		cout << endl;
	}
	return;
}

void calc_dp(int v)
{
	if (dp[v] != -1)
		return;
	long long res = 0;
	for (int i = 1; i <= N; i++)
	{
		if (way[i][v])
		{
			if (dp[i] == -1)
			{
				calc_dp(i);
			}
			res = res + dp[i];
		}
	}
	dp[v] = res;
	return;
}

void calc()
{
	for (int j = 1; j <= N; j++)
	{
		for (int i = 1; i <= N; i++)
			IN[i] = 0;
		ans = 0;
		dfs(j);
		if (ans == -1)
			return;
	}
	for (int i = 1; i <= N; i++)
		dp[i] = -1;
	dp[1] = 1;
	for (int i = 2; i < N; i++)
	{
		int res = 0;
		for (int j = 1; j <= N; j++)
		{
			if (way[j][i])
				res++;
		}
		if (res == 0)
			dp[i] = 0;
	}
	calc_dp(N);
	ans = dp[N];
	return;
}

void solve()
{
	long long one = 1;
	long long s = (N - 1) * (N - 1);
	for (long long mask = 0; mask < (one << s); mask++)
	{
		for (int i = 1; i <= N; i++)
		{
			for (int j = 1; j <= N; j++)
			{
				way[i][j] = false;
			}
		}
		for (int i = 1; i <= N - 1; i++)
		{
			for (int j = 1; j <= N; j++)
			{
				if (i != j)
				{
					int pos = (i - 1) * (N - 1);
					if (j < i)
						pos = pos + (j - 1);
					else
						pos = pos + (j - 2);
					long long p = pos - 1;
					if ((mask & (one << p)) == (one << p))
						way[i][j] = true;
				}
			}
		}
		calc();
		if (ans == K)
		{
			cout << "POSSIBLE" << endl;
			print();
			return;
		}
	}
	cout << "IMPOSSIBLE" << endl;
	return;
}

void Kate()
{
	long long one = 1;
	long long st = N - 2;
	if ((one << st) < K)
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	cout << "POSSIBLE" << endl;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
			way[i][j] = false;
	}
	if (K == 1)
	{
		way[1][N] = true;
		print();
		return;
	}
	if (K == 2)
	{
		way[1][N] = true;
		way[1][2] = true;
		way[2][N] = true;
		print();
		return;
	}
	dp[1] = 1;
	dp[2] = 1;
	long long two = 2;
	way[1][2] = true;
	for (int i = 3; i <= N; i++)
	{
		if (dp[i - 1] * two <= K)
		{
			dp[i] = dp[i - 1] * two;
			for (int j = 1; j < i; j++)
				way[j][i] = true;
		}
		else
		{
			for (int j = i - 1; j >= 1; j--)
			{
				if (K >= dp[j])
				{
					K -= dp[j];
					way[j][N] = true;
				}
			}
			break;
		}
	}
	print();
	return;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B2.txt", "w", stdout);
	int Test;
	cin >> Test;
	for (int i = 1; i <= Test; i++)
	{
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		//solve();
		Kate();
	}
	return 0;
}