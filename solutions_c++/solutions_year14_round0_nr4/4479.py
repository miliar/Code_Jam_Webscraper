#include <cstdio>
#include <algorithm>
using namespace std;

double a[1005], b[1005];
bool used[1005];
int T, N;

int whh(double p[], double q[]) {
	int cnt = 0;
	memset(used, 0, sizeof(used));
	for (int i = 0; i < N; ++i) {
		int f = -1, k = -1;
		for (int j = 0; k == -1 && j < N; ++j) {
			if (!used[j]) {
				if (f == -1) f = j;
				if (p[i] < q[j]) k = j;
			}
		}
		if (k == -1) k = f;
		used[k] = true;
		if (p[i] < q[k]) cnt++;
	}
	return cnt;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		int x = 0, y = 0;
		for (int i = 0; i < N; ++i) scanf("%lf", &a[i]);
		for (int i = 0; i < N; ++i) scanf("%lf", &b[i]);
		sort(a, a + N);
		sort(b, b + N);
		y = whh(a, b);
		x = whh(b, a);
		printf("Case #%d: %d %d\n", tc, x, N - y);
	}
	return 0;
}