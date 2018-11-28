#include <cstdio>
#include <algorithm>

using namespace std;

int A[100000];

int Work()
{
	int N, GMax = 0;
	scanf("%d", &N);
	for (int i = 0; i < N; i ++)
	{
		scanf("%d", &A[i]);
		GMax = max(GMax, A[i]);
	}
	int Ans = GMax;
	for (int G = 1; G <= GMax; G ++)
	{
		int Moves = 0;
		for (int i = 0; i < N; i ++)
			Moves += (A[i] - 1) / G;
		Ans = min(Ans, G + Moves);
	}
	return Ans;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: %d\n", Case, Work());
	}
	return 0;
}
