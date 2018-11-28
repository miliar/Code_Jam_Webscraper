#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int N_MAX = 1000;

int dane[N_MAX];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &dane[i]);
		}
		int max_diff = 0;
		for (int i = 1; i < N; ++i) {
			max_diff = max(max_diff, dane[i - 1] - dane[i]);
		}
		int a = 0, b = 0;
		for (int i = 1; i < N; ++i) {
			if (dane[i - 1] > dane[i]) {
				a += dane[i - 1] - dane[i];
			}
		}
		for (int i = 0; i < N - 1; ++i) {
			b += min(dane[i], max_diff);
		}
		printf("Case #%d: %d %d\n", t, a, b);
	}
	return 0;
}