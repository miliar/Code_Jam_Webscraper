#include <stdio.h>

char *digit[10] = { "ZERO", "SIX", "TWO", "SEVEN", "FOUR", "FIVE", "THREE", "EIGHT", "ONE", "NINE" };
int d[10] = { 0, 6, 2, 7, 4, 5, 3, 8, 1, 9  };
int count[10];
int N;
char input[3000];
char alpha[30];
char beta[30];

void find();

void main()
{
	int i, j, k, p;
	scanf("%d", &N);

	for ( i = 1; i <= N; i++) {
		scanf("%s", &input);

		for (j = 0; j < 26; j++) {
			alpha[j] = 0;
			beta[j] = 0;
		}

		for ( j = 0; input[j]; j++)
			alpha[input[j]-'A']++;

		printf("Case #%d: ", i);
		for (j = 0; j < 10; j++) {
			count[j] = 0;
		}
		for (j = 0; j < 10; j++) {
			for (p = 0; p < 26; p++) {
				beta[p] = 0;
			}
			for (k = 0; digit[j][k]; k++) {
				if (alpha[digit[j][k] - 'A'] > 0) {
					alpha[digit[j][k] - 'A']--;
					beta[digit[j][k] - 'A']++;
				}
				else
					break;
			}
			if (digit[j][k] == '\0') { // find
				count[d[j]]++;
				j--;
			}
			else {
				for (p = 0; p < 26; p++) {
					alpha[p] += beta[p];
				}
			}
		}
		for (j = 0; j < 10; j++) {
			for(p = 0; p < count[j]; p++)
				printf("%d", j);
		}
		printf("\n");
	}
}