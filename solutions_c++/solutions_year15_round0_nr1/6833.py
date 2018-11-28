#include <cstdio>
using namespace std;

int main() {
	int cases, n, ans, cnt, nti;
	char input[1005];
	scanf("%d", &cases);
	for (int c = 1; c <= cases; ++c) {
		scanf("%d %s", &n, input);
		ans = 0, cnt = input[0] - '0';
		for (int i = 1; i <= n; ++i) {
			ans += (nti = (i > cnt) ? (i - cnt) : 0);
			cnt += input[i] - '0' + nti;
		}
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}
