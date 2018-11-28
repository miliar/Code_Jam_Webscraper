#include <iostream>
#include <fstream>
#include <string.h>

#define SIZE 1005

using namespace std;

int main () {
	int caseNo;
	char S[SIZE], out[SIZE * 2 + 1];

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &caseNo);

	int c = 1;

	while (c <= caseNo) {
		scanf("%s", S);

		int len = strlen(S);
		int start = SIZE;
		int end = SIZE;

		out[start] = S[0];

		for (int i = 1; i < len; i++) {
			if (out[end] <= S[i]) {
				end++;
				out[end] = S[i];
			} else {
				start--;
				out[start] = S[i];
			}
		}

		printf("Case #%d: ", c);

		for (int i = end; i >= start; i--) {
			printf("%c", out[i]);
		}
		printf("\n");
		
		c++;
	}

	return 0;
}