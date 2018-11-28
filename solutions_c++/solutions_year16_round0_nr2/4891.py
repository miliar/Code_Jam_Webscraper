#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 120
int T;
char S[MAX];

int do_solve(int pos, char des) {
	if (pos == 0) {
		return S[0] == des ? 0 : 1;
	}
	if (S[pos] == des) {
		return do_solve(pos - 1, des);
	}
	else {
		return do_solve(pos - 1, S[pos]) + 1;
	}
}

int solve() {
	int len = strlen(S);
	return do_solve(len - 1, '+');
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%s", S);
		printf("Case #%d: ", t);
		printf("%d\n", solve());
	}
	return 0;
}