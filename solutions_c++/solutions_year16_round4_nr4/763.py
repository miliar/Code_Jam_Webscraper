#include <bits/stdc++.h>
using namespace std;

int N;
int v[5][5], m[5][5];

int test(int bm, int used)
{
	if (bm+1 == 1<<N) return (used+1 == 1<<N ? 1 : 0);
	int ans = 1, hasOpt=0;
	for (int a = 0; a < N; a++)
		if (!(bm&(1<<a)))
			for (int b = 0; b < N; b++)
				if (m[a][b]&&!(used&(1<<b)))
				{
					hasOpt=1;
					ans &= test(bm|(1<<a),used|(1<<b));
					if (!ans) return 0;
				}
	return ans&hasOpt;
}

int ok()
{
	int ans = 1, hasOpt=0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (m[i][j])
			{
				hasOpt=1;
				ans &= test(1<<i,1<<j);
				if (!ans) return 0;
			}
	return ans&hasOpt;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int ans = 99;
		char x;
		scanf("%d", &N);
		
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
			{
				scanf(" %c", &x);
				v[i][j] = x-'0';
			}
		for (int i = 0; i <= 1<<(N*N); i++)
		{
			int flag = 1, co=0;
			for (int j = 0; j < N*N; j++)
			{
				if (i & (1<<j)) m[j/N][j%N] = 1;
				else m[j/N][j%N] = 0;
				if (v[j/N][j%N]&&!m[j/N][j%N])
				{
					flag = 0;
					break;
				}
				else if (!v[j/N][j%N]&&m[j/N][j%N]) co++;
			}
			if (flag)
			{
				//for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) printf("%d%s",m[i][j],j<N-1?" ":"\n"); printf("\n");
				//printf("%d\n",co);
				if (ok())
					ans = min(ans,co);
			}
			//if (!ans) break;
		}
		printf("Case #%d: ", t);
		printf("%d\n", ans);
	}
}
