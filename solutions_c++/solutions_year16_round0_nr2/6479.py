#include<stdio.h>
#include<string.h>
int main() {

	int i, j, k, T, cnt = 0, total = 0;
	char S[105];

	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (i = 1; i <= T; i++) {
		
		for (j = 0; j < 105; j++) S[j] = NULL;
		scanf("%s", S);
		cnt = 0;
		total = 0;
		
		for (j = strlen(S) - 1; j >= 0; j--) {
			if (S[j] == '-') {
				cnt++;
				for (k = j - 1; k >= 0; k--) {
					if (S[k] == '-') S[k] = '+';
					else if (S[k] == '+') S[k] = '-';
				}
			}
		}
		printf("Case #%d: %d\n",i, cnt);


	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}