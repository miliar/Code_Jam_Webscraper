#include <cstdio>
#include <cstdlib>

using namespace std;

const int S_MAX = 100;
int S[S_MAX];

void print_result(int t, int result) {
	printf("Case #%d: %d\n", t, result);
}

void print_array(int n, int *A) {
	for (int i = 0; i < n; ++i) {
		printf("%d", A[i]);
	}
	printf("\n");
}

int solve() {
	int n = 0;
	char c;
	while ((c = getchar()) != '\n') {
		if (c == '+') S[n++] = 1;
		else S[n++] = -1;
	}
	int result = 0;
	int parz = 1;
	int l = 0, p = n - 1;
	while (l <= p) {
		if (parz) {
			while (l <= p && S[p] == 1) --p;
			if (l > p) break;
			result += S[l] == 1;
			while (l <= p && S[l] == 1) ++l;
			++result;
			while (l <= p && S[l] == -1) ++l;
		} else {
			while (l <= p && S[l] == -1) ++l;
			if (l > p) break;
			result += S[p] == -1;
			while (l <= p && S[p] == -1) --p;
			++result;
			while (l <= p && S[p] == 1) --p;
		}
		parz *= -1;
	}
	return result;
}

int main() {
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t) {
		int result = solve();
		print_result(t, result);
	}
	return 0;
}