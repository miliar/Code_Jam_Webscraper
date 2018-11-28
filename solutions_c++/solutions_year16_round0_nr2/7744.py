#include <cstdio>
#include <cstring>

void flip(char arr[], int to) {
	for (int i = 0; i <= to; ++i) {
		arr[i] = 1 - arr[i];
	}
}

char stack[128];

int main() {
	int tests, n, answer;
	scanf("%d", &tests);
	for (int case_no = 1; case_no <= tests; ++case_no) {
		scanf("%s", stack);
		n = strlen(stack);

		for (int i = 0; i < n; ++i) {
			stack[i] = stack[i] == '+' ? 1 : 0;
		}

		answer = 0;

		for (int i = n - 1; i >= 0; --i) {
			if (stack[i] == 0) {
				flip(stack, i);
				answer++;
			}
		}

		printf("Case #%d: %d\n", case_no, answer);

	}
	return 0;
}