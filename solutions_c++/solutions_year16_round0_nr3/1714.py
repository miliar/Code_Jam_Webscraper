#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n,J;
bool x[50];
int num = 0;

inline bool rec (int k) {
	if (k == n-2) {
		for (int i = 0;i < n;i ++) {
			printf ("%d", x[i]);
		}
		for (int i = 2;i <= 10;i ++) {
			printf (" %d", i+1);
		}
		printf ("\n");

		num ++;

		return (num == J);
	} else {
		x[k] = 0;
		if (rec (k+1)) {
			return true;
		}
		if (k+2 <= n-2) {
			x[k] = x[k+1] = 1;
			return rec (k+2);
		}
		return false;
	}
}

int main () {
	int t;
	scanf ("%d", &t);

	for (int i = 1;i <= t;i ++) {
		scanf ("%d %d", &n, &J);

		printf ("Case #%d:\n", i);

		x[0] = x[1] = x[n-2] = x[n-1] = 1;
		rec (2);
	}
}