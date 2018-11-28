#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
#include <climits>

const int MAX_N = 1024;
int N;
int A[MAX_N];
int f[MAX_N][MAX_N], g[MAX_N][MAX_N];

int solve2()
{
	for (int i = 0; i < N; ++i)
	{
		f[i][0] = 0;
		for (int j = 0; j < i; ++j)
		{
			f[i][j + 1] = f[i][j] + ((A[j] > A[i]) ? 1 : 0);
		}
		f[i][i + 1] = f[i][i];
		for (int j = i + 1; j < N; ++j)
		{
			f[i][j + 1] = f[i][j] + ((A[j] < A[i]) ? 1 : 0);
		}

		g[i][N] = 0;
		for (int j = N - 1; j > i; --j)
		{
			g[i][j] = g[i][j + 1] + ((A[j] > A[i]) ? 1 : 0);
		}
		g[i][i] = g[i][i + 1];
		for (int j = i - 1; j >= 0; --j)
		{
			g[i][j] = g[i][j + 1] + ((A[j] < A[i]) ? 1 : 0);
		}
	}

	int ans = N * (N - 1) / 2;
	for (int i = 0; i <= N; ++i)
	{
		int sum1 = 0, sum2 = 0;
		for (int j = 0; j < i; ++j) sum1 += f[j][i];
		for (int j = i; j < N; ++j) sum2 += g[j][i];
		//printf("i=%d sum1=%d sum2=%d\n", i, sum1, sum2);
		assert(sum1 % 2 == 0);
		assert(sum2 % 2 == 0);
		ans = std::min(ans, (sum1 + sum2) / 2);
	}
	return ans;
}

int solve()
{
	int ans = 0;
	for (int i = 0; i < N; ++i)
	{
		int which = (int)(std::min_element(A, A + N) - A);
		int step1 = 0, step2 = 0;
		for (int j = 0; j < which; ++j)
			if (A[j] < INT_MAX) ++step1;
		for (int j = which + 1; j < N; ++j)
			if (A[j] < INT_MAX) ++step2;
		ans += std::min(step1, step2);
		A[which] = INT_MAX;
	}
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &A[i]);
		}
		printf("Case #%d: %d\n", cs, solve());
	}
	return 0;
}
