//author: whd

#include <algorithm>
#include <cstdio>

#define mp make_pair
#define pb push_back

typedef long long big;
using namespace std;
int a[10020], n;
int getans(int x) {
	int s = 0;
	for (int i = 1; i <= n; i++) {
		s += (a[i] - 1) / x;
	}
	return s + x;
}
int main() {
	int cas, cass;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &cas);
	for (cass = 1; cass <= cas; cass++) {
		printf("Case #%d: ", cass);
		int i;
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		int ans = 1000;
		for (i = 1; i <= 1000; i++) {
			ans = min(ans, getans(i));
		}
		printf("%d\n", ans);
	}
}
