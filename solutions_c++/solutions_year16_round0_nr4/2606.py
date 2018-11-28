#include <cstdio>

using namespace std;

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int te = 1; te <= T; te++)
	{
		printf("Case #%d: ", te);
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		for (int i = 1; i <= k; i++) {
			printf("%d ", i);
		}
		printf("\n");
	}
	return 0;
}