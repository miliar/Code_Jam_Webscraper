#include <stdio.h>
#define MAX_S 1001
#define MAX(X, Y) (((X)>(Y))?(X):(Y))

int ans = 0;
char counts[MAX_S];
int recur(int aud) {
	if (aud <= 0) {
		return counts[0];
	}
	int subcnt = recur(aud - 1);
	int need = MAX(0, aud - subcnt);
	ans += need;
	return subcnt + counts[aud] + need;
}

int main()
{
	int T, maxs;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for (int TC = 1; TC <= T; TC++)
	{
		scanf("%d %s", &maxs, counts);
		for (int s = 0; s < maxs; s++) counts[s] -= '0';

		ans = 0;
		recur(maxs);

		printf("Case #%d: %d\n", TC, ans);
	}

	return 0;
}