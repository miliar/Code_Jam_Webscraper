#include <cstdio>

int T;
char S[101];

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T; ) {
		scanf("%s", S);

		int ans = 0;
		for (int i = 0; S[i]; ++i) {
			char c = S[i], d = S[i + 1];
			if (d == 0) d = '+';
			if (c != d) ++ans;
		}

		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
