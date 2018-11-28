#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

int n, a[MAXN];

int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		printf("Case #%d: ", _);
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) scanf("%d", a + i);
		int Ans = 0;
		for (int i = 1; i <= n; i++) {
			int A1 = 0, A2 = 0;
			for (int j = 1; j < i; j++) {
				A1 += (a[j] > a[i]);
			}
			for (int j = n; j > i; j--) {
				A2 += (a[j] > a[i]);
			}
			Ans += min(A1, A2);
		}
		printf("%d\n", Ans);
	}
	return 0;
}

