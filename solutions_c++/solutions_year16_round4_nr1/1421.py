#include <bits/stdc++.h>
using namespace std;

/*
*/

string colors;

string dp[13][3];
int A[13][3][3];

string solve(int i, int col)
{
	if (A[i][col][0] != -1)
	{
		return dp[i][col];
	}
	for (int j = 0; j < 3; j++)
		A[i][col][j] = 0;
	if (i == 0)
	{
		A[i][col][col] = 1;
		dp[i][col] = "";
		dp[i][col] += colors[col];
		return dp[i][col];
	}
	string left = solve(i-1, col);
	string right = solve(i-1, (col+1)%3);
	for (int j = 0; j < 3; j++)
	{
		A[i][col][j] = A[i-1][col][j];
		A[i][col][j] += A[i-1][(col+1) % 3][j];
	}
	if (left < right)
		return dp[i][col] = left + right;
	else
		return dp[i][col] = right + left;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("input.out", "w", stdout);
	colors = "PRS";
	int T;
	scanf("%d", &T);
	memset(A, -1, sizeof(A));
	for (int z = 1; z <= T; z++)
	{
		int n;
		int cols[3];
		scanf("%d %d %d %d", &n, cols+1, cols, cols+2);
		for (int i = 0; i < 3; i++)
			solve(n, i);
		string res = "z";
		for (int i = 0; i < 3; i++)
		{
			bool ok = true;
			for (int j = 0; j < 3; j++)
			{
				if (A[n][i][j] != cols[j])
					ok = false;
			}
			if (ok)
			{
				res = min(res, dp[n][i]);
			}
		}
		if (res == "z")
		{
			printf("Case #%d: IMPOSSIBLE\n", z);
		}
		else
		{
			printf("Case #%d: %s\n", z, res.c_str());
		}
	}
}