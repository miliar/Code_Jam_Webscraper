#include <stdio.h>

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int _n;
	scanf("%d", &_n);

	for (int _t=1; _t<=_n; _t++) {
		char s[110] = {0};
		int ret = 0, i;
		scanf("%s", s+1);
		for (i=2; s[i]; i++) {
			if (s[i-1] != s[i]) { ret++; }
		}
		if (s[i-1] == '-') { ret++; }
		printf("Case #%d: %d\n", _t, ret);
	}
}
