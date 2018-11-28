#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

const int N = 1001;

int n;

int main () {
	int i, j, k, ca, T;

	freopen ("D-large.in", "r", stdin);
	freopen ("outdlarge2.txt", "w", stdout);
	scanf ("%d", &T);
	for (ca = 1; ca <= T; ++ca) {
		//printf ("%d\n", ca);
		scanf ("%d", &n);
		vector<double>a(n), b(n);

		for (i = 0; i < n; ++i) scanf ("%lf", &a[i]);
		for (i = 0; i < n; ++i) scanf ("%lf", &b[i]);

		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int best_cheat = 0, best_fair = 0;
		i = j = n - 1;
		for (k = 0; k < n; ++k) {
			if (a[i] > b[j]) {
				best_cheat ++;
				i--; j--;
			}
			else --j;
		}

		vector<double>c(b);
		for (i = 0; i < n; ++i) {
			int m = c.size();
			if (c[m-1] < a[i]) {
				best_fair ++;
				c.erase(c.begin());
			}
			else {
				for (j = 0; j < m; ++j)
					if (c[j] > a[i]) break;
				c.erase(c.begin() + j);
			}
		}
		printf ("Case #%d: %d %d\n", ca, best_cheat, best_fair);
	}
	return 0;
}
