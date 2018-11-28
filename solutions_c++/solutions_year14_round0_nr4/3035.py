#include <cstdio>
#include <algorithm>
using namespace std;

double a[1111], b[1111];

void test() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%lf", &a[i]);
	for (int i = 0; i < n; i++) scanf("%lf", &b[i]);
	sort(a,a+n);
	sort(b,b+n);
	//for (int i = 0; i < n; i++) printf("%.3lf ", a[i]); printf("\n");
	//for (int i = 0; i < n; i++) printf("%.3lf ", b[i]); printf("\n");
	int c0 = 0, c1 = 0;
	for (int i = 0, j = 0; i < n; i++) {
		if (a[i] > b[j]) {
			j++;
			c0++;
		}
	}
	for (int i = 0, j = 0; i < n; i++) {
		while (j < n && b[j] < a[i]) {
			j++;
			c1++;
		}
		j++;
	}
	printf("%d %d\n", c0, c1);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		test();
	}
	return 0;
}
