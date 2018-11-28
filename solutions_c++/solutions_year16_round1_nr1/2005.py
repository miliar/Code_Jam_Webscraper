#include <stdio.h>

int l, r;
char s[1010], d[2020];

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%s", s);

		l = 1010; r = l;
		d[l] = s[0];

		for (int i = 1; s[i]; i++) {
			if (s[i] >= d[l]) d[--l] = s[i];
			else d[++r] = s[i];
		}
		d[++r] = 0;

		printf("Case #%d: %s\n", t, d + l);
	}

	return 0;
}

