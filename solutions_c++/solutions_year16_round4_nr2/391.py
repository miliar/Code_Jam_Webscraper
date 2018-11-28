#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 210 + 17;

#define bit(x) (1<<(x-1))

double F[N][N*2],ans,A[N];
int n,K,m,cnt,Q[N];

void Dp()
{
	memset(F, 0, sizeof F);
	F[0][K] = 1;
/*	for (int i = 0; i < n; i ++)
		for (int j = 0; j <= i && j < K; j ++)
		{
			F[i+1][j+1] += (F[i][j] * A[Q[i]], F[i+1][j+1]);
			F[i+1][j] += (F[i][j] * (1 - A[Q[i]]), F[i+1][j]);
		}
	ans = max(ans, F[i][j]);*/
	
	for(int i = 1;i <= K;i ++)
	{
		int cur = Q[i];
		for(int j = 0;j <= 2 * K;j ++)
		{
			if (j > 0) F[i][j] += F[i-1][j-1] * A[cur];
			if (j < 2 * K) F[i][j] += F[i-1][j+1] * (1 - A[cur]);
		}
	}
	ans = max(ans,F[K][K]);
}

int main()
{
///	freopen("data.in", "r", stdin);
///	freopen("data.out", "w", stdout);

	int CT; scanf("%d", &CT);

	for (int pt = 1; pt <= CT; pt ++)
	{
		printf("Case #%d: ", pt);

		scanf("%d%d", &n, &K);
		m = 1 << n;

		for (int i = 1; i <= n; i ++) scanf("%lf", &A[i]);

		sort(A + 1, A + 1 + n);

		ans = 0;
		for (int i = 0; i <= K; i ++)
		{
			int cnt = 0;
			for (int j = 1; j <= i; j ++)
				Q[++ cnt] = j;
			for (int p = 1, j = n; p + i <= K; p ++, j --)
				Q[++ cnt] = j;
			if (cnt != K) puts("");
			Dp();
		}
		printf("%.10f", ans);
		
		puts("");
	}
	return 0;
}



