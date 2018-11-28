#include <cstdio>
#include <algorithm>
using namespace std;
#define N 1234

int t, n, a[N]; char s[N];
int main() {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", a+i);
			s[i] = 0;
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int bst = -1;
			for (int j = 0; j < n; j++) if (!s[j] && (bst==-1 || a[j] > a[bst])) bst = j;
			s[bst] = 1; 
			int lft = 0, rht = 0;
			for (int j = 0; j < bst; j++) if (a[j] > a[bst]) lft++;
			for (int j = bst+1; j < n; j++) if (a[j] > a[bst]) rht++;
			ans += min(lft, rht);
		}
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}