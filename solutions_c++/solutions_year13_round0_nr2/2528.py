#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int N, M;
int A[101][101];
int CutX[101], CutY[101];

int Work(int Case)
{
	scanf("%d%d", &N, &M);
	memset(CutX, 0, sizeof(CutX));
	memset(CutY, 0, sizeof(CutY));
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < M; j ++)
		{
			scanf("%d", &A[i][j]);
			CutX[i] = max(CutX[i], A[i][j]);
			CutY[j] = max(CutY[j], A[i][j]);
		}
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < M; j ++)
			if (A[i][j] != min(CutX[i], CutY[j]))
				return 0;
	return 1;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %s\n", Case, Work(Case) ? "YES" : "NO");
	return 0;
}