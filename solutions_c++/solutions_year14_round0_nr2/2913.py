#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

double c, f, x, ans, tmp, per;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w", stdout);
	int cas; scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		cin >> c >> f >> x; ans = x / 2; tmp = 0; per = 2;
		while (tmp - ans < 1e-6) {
			tmp += c / per; per += f;
			ans = min(ans, tmp + x / per);
		}
		printf("Case #%d: %.7f\n", t, ans);
	}
	return 0;
}

