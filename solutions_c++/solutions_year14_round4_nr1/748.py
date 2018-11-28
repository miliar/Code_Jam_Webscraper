#include <cstring>
#include <iostream>
using namespace std;
const int MOD = 1000000007;
int testCase, n, m, a[111111];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testCase);
	for (int Case = 1; Case <= testCase; Case ++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i ++) {
			scanf("%d", &a[i]);
		}
		sort(a, a + n);
		int ret = 0;
		for (int l = 0, r = n - 1; l <= r; r --) {
			ret ++;
			if (a[l] + a[r] <= m) {
				l ++;
			}
		}
		printf("Case #%d: %d\n", Case, ret);
	}
	return 0;
}
