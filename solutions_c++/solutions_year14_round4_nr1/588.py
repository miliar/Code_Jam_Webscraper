#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

int cas, n, m, x, y;
int a[800];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		scanf("%d%d", &n, &x);
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; i++) {
			scanf("%d", &m); ++a[m];
		}
		m = 0;
		for (int i = x; i > 0; i--) {
			while (a[i] > 0) {
				++m; --a[i]; y = x - i;
				while (y > 0 && a[y] == 0) --y;
				if (y > 0) --a[y];
			}
		}
		printf("Case #%d: %d\n",t, m);
	}
	return 0;
}

