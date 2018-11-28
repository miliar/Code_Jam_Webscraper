#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int v[1005];
pair<int, int> r[1005];

void work() {
    int n; scanf("%d", &n);
    memset(v, 0, sizeof(v));
    for (int i = 1; i <= n; ++i) scanf("%d", &v[i]);
    for (int i = 1; i <= n; ++i) r[i] = make_pair(v[i], i);
    sort(r + 1, r + n + 1);

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
		int a = 0, b = 0, k = r[i].second, t = r[i].first;
		for (int j = 1; j < k; ++j) if (v[j] > t) a++;
		for (int j = k + 1; j <= n; ++j) if (v[j] > t) b++;
		ans += min(a, b);
    }

	printf("%d\n", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
