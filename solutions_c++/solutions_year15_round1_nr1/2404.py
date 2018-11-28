#include <cstdio>
#include <algorithm>
using namespace std;
main()
{
	int t, n, m[1000], r, y, z;
	scanf("%d", &t);
	for (int x = 1 ; x <= t ; ++x) {
		y = z = r = 0;
		scanf("%d", &n);
		for (int i = 0 ; i < n ; ++i) scanf("%d", &m[i]);
		for (int i = 1 ; i < n ; ++i) {
			r = max(m[i - 1] - m[i], r);
			y += max(m[i - 1] - m[i], 0);
		}
		for (int i = 0 ; i < n - 1 ; ++i) z += min(m[i], r);
		printf("Case #%d: %d %d\n", x, y, z);
	}
}