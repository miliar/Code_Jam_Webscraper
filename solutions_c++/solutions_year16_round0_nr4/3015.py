#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <set>
#include <vector>
#include <string.h>

using namespace std;

int cmp(const void *x, const void *y) {
	// Implement when needed
	return 0;
}

int cmp(const int x, const int y) {
	return x - y;
}

int cmp(const double x, const double y) {
	return x - y;
}

int cmp(const char *x, const char *y) {
	int s1 = x ? strlen(x) : 0;
	int s2 = y ? strlen(y) : 0;
	if (s1 != s2) return s1 - s2;
	if (!s1) return 0;
	return strcmp(x, y);
}

int cmp(const string x, const string y) {
	return x.compare(y);
}

#define MAX(x, y) (cmp((x), (y)) > 0 ? (x) : (y))
#define MIN(x, y) (cmp((x), (y)) < 0 ? (x) : (y))

int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		int k, c, s, start;
		cin >> k >> c >> s;

		cout << "Case #" << i + 1 << ":";

		if (k == 1) {
			if (s >= 1) cout << " 1" << endl;
			else cout << " IMPOSSIBLE" << endl;
			continue;
		}

		if ((c == 1 && k != s) || (c > 1 && s < k - 1)) {
			cout << " IMPOSSIBLE" << endl;
			continue;
		}

		start = (c == 1) ? 1 : 2;
		for (int i = start; i <= k; i++) cout << " " << i;
		cout << endl;
	}

	return 0;
}

