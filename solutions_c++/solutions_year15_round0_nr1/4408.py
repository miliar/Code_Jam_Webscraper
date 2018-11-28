#include <bits/stdc++.h>

const int N = 1001;

int smax;
char shynum[N + 1];

int solve() {
	int result = 0, sum = shynum[0] - '0';
	for (int i = 1; shynum[i]; ++i) {
		if (i > sum + result)
			result += i - (sum + result);
		sum += shynum[i] - '0';
	}
	return result;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int cnum = 1; cnum <= t; ++cnum) {
		scanf("%d %s", &smax, shynum);
		printf("Case #%d: %d\n", cnum, solve());
	}
	return 0;
}
