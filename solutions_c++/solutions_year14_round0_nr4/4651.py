#include <stdio.h>
#include <algorithm>
#include<vector>
#include <string.h>

using namespace std;

int main (void) {
	int t, c;
	int n, i, j;
	double a[1000], b[1000];
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		printf ("Case #%d: ", c);
		scanf ("%d", &n);
		for (i = 0; i < n; i++)	scanf ("%lf", &a[i]);
		for (i = 0; i < n; i++)	scanf ("%lf", &b[i]);
		sort(a, a+n);
		sort(b, b+n);
//		for (i = 0; i < n; i++)	printf ("%lf ", a[i]); printf ("\n");
//		for (i = 0; i < n; i++)	printf ("%lf ", b[i]); printf ("\n");
		int ans1 = n, ans2 = 0;
		bool ok = true;
		for (i = 1; i <= n && ok; i++) {
			for (j = 0; j < i && ok; j++) {
				if (a[n-i+j] < b[j]) {
					ans1 = i-1;
					ok = false;
				}
			}
		}
		bool used[1000];
		memset (used, 0, sizeof used);
		for (i = 0; i < n; i++) {
			j = 0;
			while (j < n && (used[j] || b[j] < a[i]))	j++;
			if (j == n) {
				while (j < n && used[j])	j++;
				used[j] = true;
				ans2++;
			} else
				used[j] = true;
		}

		printf ("%d %d\n", ans1, ans2);
	}
	return 0;
}
