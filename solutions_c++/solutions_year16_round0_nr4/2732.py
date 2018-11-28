#include <cstdio>
#include <cstdlib>

using namespace std;

void special_case(int K, int S) {
	for (int i = 1; i <= S; ++i) {
		printf("%lld", i);
		if (i < S) printf(" ");
	}
	printf("\n");
}

void solve(int t) {
	int K, C, S;
	scanf("%d %d %d", &K, &C, &S);
	printf("Case #%d: ", t);
	if (C == 1) {
		special_case(K, S);
		return;
	}
	long long int KC = 1;
	for (int i = 0; i < C; ++i) {
		KC *= K;
	}
	long long int j = 1;
	for (int i = 0; i < S && j <= KC; ++i) {
		printf("%lld", j);
		j += K;
		if (i < S - 1 && j <= KC) printf(" ");
	}
	printf("\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		solve(t);
	}
	return 0;
}