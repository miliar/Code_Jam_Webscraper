#include <cstdio>
#include <algorithm>
using namespace std;
int s[10010];
int main() {
	int testnum, n, x, first, ans;
	scanf("%d", &testnum);
	for (int test = 1; test <= testnum; test++) {
		scanf("%d%d", &n, &x);
		for (int i = 0;i < n;i++) {
			scanf("%d", &s[i]);
		}
		sort(s, s + n);
		first = 0;
		ans = 0;
		for (int i = n - 1;i >= first;i--) {
			if (i > first && s[i] + s[first] <= x) {
				ans++;
				first++;
			} else if (i == first) {
				ans++;
			} else {
				ans++;
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
