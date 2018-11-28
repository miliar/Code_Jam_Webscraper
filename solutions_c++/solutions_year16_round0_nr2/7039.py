#include <cstdio>
#include <cstring>

int main () {
	freopen("B-large.in", "r", stdin);
	// freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t)
	{
		char c = 0;
		int n, ans = 0;
		int a[100];
		scanf("%c", &c);
		for (n = 0; c != '\n'; ++n)
		{
			if (c == '+')
				a[n] = 1;
			else
				a[n] = 0;
			scanf("%c", &c);
		}
		// fprintf(stderr, "%d\n", n);
		// for (int i = 0; i < n; ++i)
		// 	fprintf(stderr, "%d\t", a[i]);
		// fprintf(stderr, "\n");

		for (int i = n - 1; i > 0; --i)
			if (a[i] == 0)
			{
				if (a[0] == 0)
					++ans;
				else
				{
					ans += 2;
					for (int j = 0; j < i && a[j] == 1; ++j)
						a[j] = 0;
				}
				for (int j = 0; j < (i + 1) / 2; ++j)
				{
					int tmp = a[j]; a[j] = a[i - j]; a[i - j] = tmp;
				}
				for (int j = 0; j <= i; ++j)
					a[j] = 1 - a[j];
		// for (int i = 0; i < n; ++i)
		// 	fprintf(stderr, "%d\t", a[i]);
		// fprintf(stderr, "\n");
		// fprintf(stderr, "%d\n", ans);
			}
		//case 0
		if (a[0] == 0)
			++ans;
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}