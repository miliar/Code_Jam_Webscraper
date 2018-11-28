#include<stdio.h>
#include<string.h>

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, T;
	char s[2000] = { 0 };
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		int i, j, k, len, cnt=0;
		bool flag = false;
		scanf("%s %d", s, &k);
		len = strlen(s);
		for (i = 0; i < len; i++) {
			if (i + k > len) {
				if (s[i] == '-') {
					flag = true;
					break;
				}
				continue;
			}
			if (s[i] == '-') {
				for (j = 0; j < k; j++) {
					if (s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				}
				cnt++;
			}
		}
		if (!flag) printf("Case #%d: %d\n", t, cnt);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}