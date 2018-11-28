#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MAX = 10000000;
int memo[MAX+1];

const int DIGITS = 20;
char buffer[DIGITS];

bool is_palindrome(long long num) {
	sprintf(buffer, "%lld", num);
	int n = strlen(buffer);
	for (int i = 0; i < n/2; i++) {
		if (buffer[i] != buffer[n-i-1]) {
			return false;
		}
	}
	return true;
}

void pre_compute() {
	memo[0] = 0;
	for (int i = 0; i <= MAX; i++) {
		memo[i] = memo[i-1];
		if (is_palindrome(i) && is_palindrome(((long long) i) * ((long long) i))) {
			memo[i]++;
		}
	}
}

int main() {
	pre_compute();
	int tt;
	scanf("%d", &tt);
	long long a, b, sqa, sqb;
	for (int t = 1; t <= tt; t++) {
		scanf("%lld %lld", &a, &b);
		sqa = (long long) sqrt((double) a);
		if (sqa * sqa < a) {
			sqa++;
		}
		sqb = (long long) sqrt((double) b);
		int total = memo[sqb] - memo[sqa-1];
		printf("Case #%d: %d\n", t, total);
	}

	return 0;
}