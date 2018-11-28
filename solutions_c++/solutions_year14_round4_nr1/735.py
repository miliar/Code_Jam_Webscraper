#include <algorithm>
#include <cstdio>
#include <queue>

using std::sort;
using std::deque;

const int MaxN = 11111;

int T, N, X, a[MaxN], cs;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &T);
	while(T--) {
		int ans = 0;
		scanf("%d%d", &N, &X);
		for(int i = 1; i <= N; ++i) {
			scanf("%d", a + i);
		}
		sort(a + 1, a + 1 + N);
		for(int f = 1, t = N; f <= t;) {
			if(f != t && a[f] + a[t] <= X) {
				++f;
				--t;
				++ans;
			}
			else {
				--t;
				++ans;
			}
		}
		printf("Case #%d: %d\n", ++cs, ans);
	}
	return 0;
}