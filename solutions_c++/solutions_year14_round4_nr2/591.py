#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

int cas, n, a[1100], ans, l, r, m;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		l = 0; r = n - 1; ans = 0;
		while (l <= r) {
			m = l;
			for (int i = l + 1; i <= r; i++) 
				if (a[m] > a[i]) m = i;
			if (m - l < r - m) {
				ans += m - l;
				for (int i = m; i > l; i--) a[i] = a[i - 1];
				++l;
			} else {
				ans += r - m;
				for (int i = m; i < r; i++) a[i] = a[i + 1];
				--r;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

