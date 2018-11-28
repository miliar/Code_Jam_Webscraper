#include <cstdio>

bool is_palindrome(int x) {
	int n = x;
	int rev = 0;
	while (x > 0) {
		int d = x % 10;
		rev = rev * 10 + d;
		x /= 10;
	}

	return (n == rev);
}

int NUMBERS[1001];

int main () {
	int T;
	scanf("%d", &T);

	for(int i = 0; i < 1001; i++) NUMBERS[i] = 0;

	for(int x = 1; x < 32; x++) {
		NUMBERS[x] += NUMBERS[x-1];
		if (is_palindrome(x) && is_palindrome(x*x)) {
			NUMBERS[x*x]++;
		}
	}
	for(int x = 32; x < 1001; x++) {
		NUMBERS[x] += NUMBERS[x-1];
	}

	for(int case_num = 1; case_num <= T; case_num++) {
		int a, b;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", case_num, NUMBERS[b]-NUMBERS[a-1]);
	}

	return 0;
}
