#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int MAXN = 205;
int T, N, K;
ld P[MAXN];
ld P1[MAXN];
ld dpA[MAXN][MAXN];
ld dpB[MAXN][MAXN];

ld go()
{
	ld best = 0;
	for (int k = 0; k < N; k++)
	{
		for (int x = 1; x <= N; x++)
			P1[x] = P[(x + k) % N + 1];

		for (int i = 0; i < MAXN; i++)
			for (int j = 0; j < MAXN; j++)
				dpA[i][j] = dpB[i][j] = 0.0;
		dpA[0][0] = dpB[0][0] = 1;

		for (int i = 1; i <= K / 2; i++)
			for (int j = 0; j <= i; j++)
			{
				if (j > 0)
					dpA[i][j] = dpA[i - 1][j] * (1 - P1[i]) + dpA[i - 1][j - 1] * P1[i];
				else
					dpA[i][j] = dpA[i - 1][j] * (1 - P1[i]);
			}

		for (int i = N - K / 2 + 1; i <= N; i++)
		{
			int i1 = i - N + K / 2;
			for (int j = 0; j <= i1; j++)
			{
				if (j > 0)
					dpB[i1][j] = dpB[i1 - 1][j] * (1 - P1[i]) + dpB[i1 - 1][j - 1] * P1[i];
				else
					dpB[i1][j] = dpB[i1 - 1][j] * (1 - P1[i]);
			}
		}

		ld ans = 0;
		for (int i = 0; i <= K / 2; i++)
			ans += dpA[K / 2][i] * dpB[K / 2][K / 2 - i];
		best = max(best, ans);
	}
	return best;
}

ld dp1[MAXN][MAXN];
int A[MAXN];

ld go1()
{
	ld best = 0;
	for (int i = 0; i < (1 << N); i++)
	{
		int cnt = 0;
		for (int j = 0; j < N; j++)
			if ((i & (1 << j)))
				A[++cnt] = j + 1;

		if (cnt != K)
			continue;

		for (int i = 0; i < MAXN; i++)
			for (int j = 0; j < MAXN; j++)
					dp1[i][j] = 0.0;

		dp1[0][0] = 1;

		for (int i = 1; i <= K; i++)
				for (int j = 0; j <= i; j++)
				{
					if (j > 0)
						dp1[i][j] = max(dp1[i][j], dp1[i - 1][j] * (1 - P[A[i]]) + dp1[i - 1][j - 1] * P[A[i]]);
					else
						dp1[i][j] = max(dp1[i][j], dp1[i - 1][j] * (1 - P[A[i]]));
				}
		best = max(best, dp1[K][K / 2]);
	}
	return best;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	ios::sync_with_stdio(0);

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> N >> K;
		for (int i = 1; i <= N; i++)
			cin >> P[i];
		sort(P + 1, P + N + 1);

		//ld ans = go(), ans1 = go1();
		//printf("Case #%d: %.10f\n", t, (double)ans1);
		//if (abs(ans - ans1) > 1E-6)
			//cout << "OOPS\n";
		printf("Case #%d: %.10f\n", t, (double)go());
	}

	return 0;
}