#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

#pragma comment(linker, "/STACK:268435456")

typedef pair<int, int> pii;
typedef long long ll;

void solve() {
	double c, f0, x;
	scanf("%lf%lf%lf", &c, &f0, &x);

	double ans = x / 2;
	double t = 0;
	double f = 2;

	for (int i = 0; i < 1e6; i++) {
		if (c / f > x / f || t > ans)
			break;
		t += c / f;
		f += f0;
		ans = min(ans, t + x / f);
	}
	
	printf("%.10lf\n", ans);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("outut.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int i = 1; i <= T; ++i) {
    	printf("Case #%d: ", i);
		solve();
    }

	return 0;
}
