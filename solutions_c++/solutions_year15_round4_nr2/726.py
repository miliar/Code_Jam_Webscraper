#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int T, n;
double V, C, r[105], c[105];

int main(int argc, char** argv) {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	for (int times=0; times<T; times++) {
		printf("Case #%d: ", times+1);
		scanf("%d%lf%lf", &n, &V, &C);
		for (int i=0; i<n; i++) scanf("%lf%lf", &r[i], &c[i]);
		
		if (n == 1) {
			if (C != c[0]) printf("IMPOSSIBLE\n");
			else printf("%.8lf\n", V/r[0]);
			continue;
		}
		if (c[0] == c[1]) {
			if (c[0] != C) printf("IMPOSSIBLE\n");
			else printf("%.8lf\n", V/(r[0]+r[1]));
			continue;
		}
		
		if (c[0]<C && c[1]<C) printf("IMPOSSIBLE\n");
		else if (c[0]>C && c[1]>C) printf("IMPOSSIBLE\n");
		else {
			double t2 = (V*C - V*c[0]) / r[1] / (c[1] - c[0]);
			double t1 = (V - t2 * r[1]) / r[0];
			printf("%.8lf\n", t1>t2?t1:t2);
		}
	}
	return 0;
}

