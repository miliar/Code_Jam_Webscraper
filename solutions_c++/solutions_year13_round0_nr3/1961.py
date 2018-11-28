#include <cstdio>

long long getPalindrome(long long n, int mid) {
	long long result = n;
	if (mid != -1) {
		result *= 10;
		result += mid;
	}
	while (n != 0) {
		result *= 10;
		result += n % 10;
		n /= 10;
	}
	return result;
}

bool isPalindrome(long long n) {
	static int b[32];
	int c = 0;
	while (n != 0) {
		b[c++] = n % 10;
		n /= 10;
	}

	for (int i = 0; 2 * i < c; i++) {
		if (b[i] != b[c - 1 - i]) {
			return false;
		}
	}

	return true;
}

int count(long long n) {
	int result = 0;

	for (int i = 0; ; i++) {
		// Even
		long long p = getPalindrome(i, -1);
		long long p2 = p * p;
		if (p2 > n) {
			break;
		}
		if (p2 > 0 && isPalindrome(p2)) {
			result++;
		}

		// Odd
		for (int mid = 0; mid <= 9; mid++) {
			p = getPalindrome(i, mid);
			p2 = p * p;
			if (p2 > n) {
				break;
			}
			if (p2 > 0 && isPalindrome(p2)) {
				result++;
			}
		}
	}

	return result;	
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ti++) {
		long long a, b;
		scanf("%lld%lld", &a, &b);
		printf("Case #%d: %d\n", ti, count(b) - count(a - 1));
	}
	return 0;
}

