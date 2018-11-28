#include <cstdio>
int main()
{
	int T;
	int a, b, k;
	//freopen("E:\\My Code\\GCJ\\R1B\\B-small-attempt0.in", "r", stdin);
	//freopen("E:\\My Code\\GCJ\\R1B\\B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int ans = 0;
		scanf("%d%d%d", &a, &b, &k);
		for (int i = 0; i < a; ++i)
			for (int j = 0; j < b; ++j)
				if ((i&j) < k) ++ans;
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}