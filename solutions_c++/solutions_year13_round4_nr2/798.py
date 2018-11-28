#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAXN = 1024+5;
int T, N, P, lst[MAXN], rnd[MAXN];
bool vis[MAXN];
int main()
{
	freopen("put.in", "r", stdin);
	freopen("put.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++)
	{
		scanf("%d%d", &N, &P);
		for (int i = 0; i < (1<<N); i++)
		{
			lst[i] = i;
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < (1<<i); j++)
			{
				int n = ((1<<N)>>i);
				for (int k = 0; k < n; k += 2)
				{
					rnd[j*n+k/2] = lst[j*n+k];
					rnd[j*n+k/2+(n>>1)] = lst[j*n+k+1];
				}
			}
			memcpy(lst, rnd, sizeof(rnd));
//			for (int k = 0; k < (1<<N); k++)
//				printf("%d ", lst[k]);
//			printf("\n");
			memset(vis, 0, sizeof(vis));
		}
		for (int k = 0; k < P; k++)
		{
			vis[lst[k]] = 1;
		}
		int ans1, ans2;
		for (int k = 0; k < (1<<N); k++)
		{
			if (vis[k])
				ans1 = k;
			else
				break;
		}
		for (int k = 0; k < (1<<N); k++)
		{
			if (vis[k])
				ans2 = k;
		}
		printf("Case #%d: %d %d\n", cas, ans1, ans2);
	}
	return 0;
}
