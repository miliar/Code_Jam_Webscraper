#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int dfs(char *str, int l) {
	int b = l-1, b2;
	while (b>=0 && str[b]=='+')
		--b;
	if (b<0)
		return 0;
	l=b+1;
	while (b>=0 && str[b]=='-')
		--b;
	if (b<0)
		return 1;
	b2 = b;
	while (b2>=0 && str[b2]=='+')
		--b2;
	if (b2<0)
		return 2;
	return dfs(str, b2+1)+2;
}

int main() {
	int T, C;
	static char str[1001];
	scanf("%d", &T);
	for (C=1; C<=T; ++C) {
		scanf("%s", str);
		int l = strlen(str);
		printf("Case #%d: %d\n", C, dfs(str, l));
	}
	return 0;
}

