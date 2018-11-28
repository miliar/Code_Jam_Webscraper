#include <cstdio>
#include <vector>

using namespace std;

int BestPlay(vector<double> &A, vector<double> &B) {
	int ta = A.size()-1, win = 0;

	for (int i = B.size()-1; i>=0; --i) 
		if (A[ta] - B[i] > -1e-7) {
			--ta;
			++win;
		}

	return win;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t) {
		int N;
		scanf("%d", &N);

		vector<double> A(N), B(N);
		for (int i=0; i<N; ++i) scanf("%lf", &A[i]); sort(A.begin(), A.end());
		for (int i=0; i<N; ++i) scanf("%lf", &B[i]); sort(B.begin(), B.end());

		int deci_opt = BestPlay(A, B);
		int war_opt = N - BestPlay(B, A);

		printf("Case #%d: %d %d\n", t+1, deci_opt, war_opt);
	}
	return 0;
}
