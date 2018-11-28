#include <cstdio>
#include <cstring>

using namespace std;

int a[1111];

void work() {
	int n; scanf("%d", &n);
	for (int i = 0; i < n; ++i) scanf("%d", &a[i]);

	int ans = 1000000000;
	for (int i = 1; i <= 1000; ++i) {
		int cur = i;
		for (int j = 0; j < n; ++j) cur += (a[j] + i - 1) / i - 1;
		if (cur < ans) ans = cur;
	}

	printf("%d\n", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}

	return 0;
}
