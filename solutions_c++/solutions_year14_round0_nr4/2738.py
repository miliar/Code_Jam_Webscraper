#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;
const int N = 1005;

int n, ansA, ansB;
double a[N], b[N];

void init () {
	ansA = ansB = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%lf", &a[i]);
	for (int i = 0; i < n; i++)
		scanf("%lf", &b[i]);
	sort(a, a + n);
	sort(b, b + n);
}

void solve () {
	int p, q;
	p = n-1;
	for (int i = n-1; i >= 0; i--) {
		if (a[p] > b[i]) {
			p--;
			ansA++;
		}
	}

	p = q = 0;
	while (p < n && q < n) {
		if (a[p] < b[q]) {
			ansB++;
			p++;
		}
		q++;
	}
	ansB = n - ansB;
}

int main () {
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; i++) {
		init ();
		solve ();
		printf("Case #%d: %d %d\n", i, ansA, ansB);
	}
	return 0;
}
