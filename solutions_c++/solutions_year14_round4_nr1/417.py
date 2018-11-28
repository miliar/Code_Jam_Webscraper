#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAX_N = 10000;

int N, X;
int S[MAX_N];

bool check(int m)
{
	for (int i = 0; i < m; ++i)
	{
		if (S[i] + S[m * 2 - 1 - i] > X) return false;
	}
	return true;
}

int solve()
{
	std::sort(S, S + N);
	int st = 0, ed = N / 2;
	while (st <= ed)
	{
		int md = (st + ed) / 2;
		if (check(md))
		{
			st = md + 1;
		}
		else
		{
			ed = md - 1;
		}
	}
	return N - ed;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		scanf("%d%d", &N, &X);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &S[i]);
		}
		printf("Case #%d: %d\n", cs, solve());
	}
	return 0;
}
