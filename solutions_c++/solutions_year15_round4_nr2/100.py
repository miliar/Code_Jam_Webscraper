#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;

double X, Y, x[110], y[110], ans, x1, x2, y1, y2, xx1, xx2;
int n, T;


int main() {
	scanf("%d", &T);
	for (int xxx = 1; xxx <= T; xxx++) {
		scanf("%d%lf%lf", &n, &X, &Y);
		for (int i = 1; i <= n; i++)
			scanf("%lf%lf", &x[i], &y[i]);
		ans = 1e9;
		for (int i = 1; i <= n; i++)
			if (Y == y[i]) ans = min(ans, X / x[i]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j < i; j++)
				if (y[i] != y[j]) {
					xx1 = (X * Y - X * y[j]) / (y[i] - y[j]);
					xx2 = X - xx1;
					if (0 <= xx1 && 0 <= xx2) ans = min(ans, max(xx1 / x[i], xx2 / x[j]));
				}else if (y[i] == Y) ans = min(ans, X / (x[i] + x[j]));
		if (ans > 1e8) printf("Case #%d: IMPOSSIBLE\n", xxx);
		else printf("Case #%d: %.9lf\n", xxx, ans);
	}
}
