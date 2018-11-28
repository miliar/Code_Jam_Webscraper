#include <cstdio>
#include <cstdlib>
#include <algorithm>

const int N = 1005;
int test, tt, n, a[N];

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--) {
		scanf("%d", &n);
		int l = 1, r = 1;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a[i]);
			r = std :: max(r, a[i]);
		}
		
		int ans = r;
		for (int i = l; i <= r; i++) {
			int s = 0;
			for (int j = 1; j <= n; j++) {
				s += (a[j] - 1) / i;
			}
			
			ans = std :: min(ans, s + i);
		}
		
		printf("Case #%d: %d\n", ++tt, ans);
	}
	
	return 0;
}

