#include <stdio.h>
#include <string.h>
int main() {

	freopen("input.txt", "rt",stdin);
	freopen("output.txt", "wt", stdout);
	int n, cost=0;
	char S[102];
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		cost = 0;
		scanf("%s", S);
		int len = strlen(S);
		S[len] = '+';
		S[len + 1] = '\0';
		for (int i = len-1; i >=0; i--) {
			if (S[i + 1] != S[i])
				cost += 1;
		}
		printf("Case #%d: %d\n",i, cost);
	}
	return 0;
}