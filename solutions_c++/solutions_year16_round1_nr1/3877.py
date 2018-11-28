#include <stdio.h>

int N;
int tc;
char input[4000];
char output[4000];

int main()
{
	int i;
	int start;
	int end;

	scanf("%d", &N);

	for (tc = 1; tc <= N; tc++) {
		scanf("%s", input);

		start = 2000;
		end = 2000;
		output[start] = input[0];
		for (i = 1; input[i]; i++) {
			if (input[i] >= output[start]) {
				start--;
				output[start] = input[i];
			}
			else {
				end++;
				output[end] = input[i];
			}

		}
		output[end + 1] = '\0';
		printf("Case #%d: %s\n", tc, output + start);
	}
}