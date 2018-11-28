#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;

int t, cnt;
double c, f, x, r[200001], ans, tt;

double tk(int k) {
	if (r[k] != 0.0f)
		return r[k];
	
	return r[k] = tk(k-1) - (x / (2.0+(k-1)*f)) + (c / (2.0+(k-1)*f)) + (x / (2.0+k*f));
}

int main() {

	scanf("%d", &t);
	for (int cc = 1; cc <= t; cc++) {
		printf("Case #%d: ", cc);

		cin >> c >> f >> x;
		memset(r, 0, sizeof r);
		r[0] = x / 2.0f;

		cnt = 0;
		ans = r[0];
		// printf("%d %.7f\n", cnt, ans);
		while (1) {
			cnt++;
			tt = tk(cnt);
			// printf("%d %.7f\n", cnt, tt);
			if ((tt = tk(cnt)) < ans)
				ans = tt;
			else
				break;
		}
		printf("%.7f\n", ans);
	}

	return 0;
}