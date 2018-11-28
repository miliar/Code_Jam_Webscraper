#include <stdio.h>
#include <string.h>
using namespace std;

int process(char * input) {
	int len = strlen(input);
	int res = 0;
	for (int i = len - 1; i >= 0; i--) {
		if (input[i] == '-') {
			int j = 0;
			for (; j < i; j++) {
				if (input[j] == '-') break;
				else input[j] = '-';
			}
			if (j > 0) res++;
			for (int p = 0, q = i; p <= q; p++, q--) {
				int tmp = input[p];
				if (input[q] == '-') input[p] = '+';
				else if (input[q] == '+') input[p] = '-';
				if (tmp == '-') input[q] = '+';
				else if (tmp == '+') input[q] = '-';
			}
			res++;
		}
	}
	return res;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0 ; t < T; t++) {
		char input[110];
		scanf("%s", input);
		int result = process(input);
		printf("Case #%d: %d\n", t + 1, result);
	}
}