#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX_N = 101000;

int n;
int a[MAX_N];

int main() {
	int T;
	scanf("%d", &T);
	freopen("a.out", "w", stdout);
	int cas = 0;
	while (T-- > 0) {
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
		long long ans = 0;
		long long up = 0;
		for (int i = 2; i <= n; ++i) if (a[i] < a[i - 1]) {
			ans += a[i - 1] - a[i];
			up = max(up, (long long)a[i - 1] - a[i]);
		}
		long long ret = 0;
		for (int i = 1; i < n; ++i) ret += min(up, (long long)a[i]);
		printf("Case #%d: %lld %lld\n", ++cas, ans, ret);
	}
	return 0;
}

