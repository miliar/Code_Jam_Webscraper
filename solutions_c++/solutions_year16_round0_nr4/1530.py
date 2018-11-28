#include <cstdio>
long long idx;
int main(void)
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int T, C, K, S;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		idx = 1;
		scanf("%d%d%d", &K, &C, &S);
		for (int i = 1; i < C; i++)
			idx *= (long long)K;
		printf("Case #%d: ", t + 1);
		for (int i = 0; i < S; i++)
			printf("%lld ", idx*i + 1);
		printf("\n");
	}
}