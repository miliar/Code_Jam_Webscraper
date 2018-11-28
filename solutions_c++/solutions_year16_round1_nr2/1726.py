#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

int n, m, i, j, T, ti, r;
int ans[52], ct[2502];

int main() {
	//freopen("./b.in", "r", stdin);
	//freopen("./b.out", "w", stdout);
	scanf("%d", &T);
	for (ti = 1; ti <= T; ++ti) {
		cin >> n;
		for (i = 1; i <= 52; ++i) ans[i] = 0;
		for (i = 1; i <= 2500; ++i) ct[i] = 0;

		int ec = 2 * n * n - n;
		for (i = 1; i <= ec; ++i) {
			cin >> r;
			ct[r]++;
		}
		i = 1;
		for (j = 1; j <= 2500; j++)
			if (ct[j] % 2 == 1) {
				ans[i] = j;
				i++;
			}
		printf("Case #%d: ", ti);
		for (i = 1; i <= n; ++i)
			printf("%d ", ans[i]);
		printf("\n");
	}
	return 0;
}
