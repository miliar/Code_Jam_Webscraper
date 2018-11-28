#include <cstdio>
#include <algorithm>
using namespace std;

int N, M;
int A[109][109];
int mr[109];
int mc[109];

void solve() {
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			if (mr[i] > A[i][j] && mc[j] > A[i][j]) {
				printf("NO\n");
				return;
			}
	printf("YES\n");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		// input
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				scanf("%d", &A[i][j]);

		// init
		for (int i = 0; i < N; ++i) mr[i] = 0;
		for (int j = 0; j < M; ++j) mc[j] = 0;

		// calculate maxima
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j) {
				mr[i] = max(mr[i], A[i][j]);
				mc[j] = max(mc[j], A[i][j]);
			}

		// check
		printf("Case #%d: ", Ti);
		solve();
	}
	return 0;
}