#include <cstdio>
#include <algorithm>
using namespace std;
int a[10005];
int T, N, X;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%d", &N, &X);
		for (int i =  0; i< N;++i) {
			scanf("%d", &a[i]);
		}
		sort(a, a+N);
		int i;
		int j = 0;
		int ans = 0;
		for (i = N - 1; i >= 0 && i > j; --i) {
			if (a[i] + a[j] <= X) {
				++j; ++ans;
			} else {
				++ans;
			}
		}
		if (i == j) ++ans;
		printf("Case #%d: %d\n", tc,  ans);
	}
	return 0;
}
