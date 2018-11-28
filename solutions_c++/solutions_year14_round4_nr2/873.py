#include <stdio.h>
#include <algorithm>

int A[1000];
int solve() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &A[i]);
	}
	int res = 0;
	for (int i = N; i > 0; i--) {
		int mn = 0;
		for (int j = 0; j < i; j++) {
			if (A[j] < A[mn]) mn = j;
		}
		res += std::min(mn, i - 1 - mn);
		for (int j = mn + 1; j < i; j++) A[j - 1] = A[j];
	}
	return res;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int c = 1; c <= T; c++) {
		printf("Case #%d: %d\n", c, solve());
	}
}