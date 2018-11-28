#include <cstdio>
#include <algorithm>

double A[1000], B[1000];

int main() {
	int N;
	scanf("%d", &N);
	for (int T = 1; T <= N; T++) {
		int L;
		scanf("%d", &L);
		for (int i = 0; i < L; i++) scanf("%lf", A+i);
		for (int i = 0; i < L; i++) scanf("%lf", B+i);

		std::sort(A, A+L);
		std::sort(B, B+L);

		int d = 0, w = 0;
		// Deceitful
		for (int i = 0; i < L; i++) {
			if (A[i] > B[d])
				d++;
		}
		// War
		for (int i = 0; i < L; i++) {
			if (B[i] > A[w])
				w++;
		}
		w = L-w;

		printf("Case #%d: %d %d\n", T, d, w);
	}
	return 0;
}
