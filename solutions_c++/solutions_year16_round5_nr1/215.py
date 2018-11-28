#include <stdio.h>
#include <string.h>
#include <string>

char str[20010];
char st[20010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int S;
		scanf("%d", &S);
		scanf(" %s", str);
		int n = strlen(str);
		int cur = 0;
		int res = 0;
		for (int i=0; i<n; i++) {
			if (cur == 0 || st[cur] != str[i]) {
				cur++;
				st[cur] = str[i];
			} else {
				cur--;
				res += 10;
			}
		}
		res += cur / 2 * 5;
		printf("Case #%d: %d\n", t, res);
	}

	return 0;
}