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
	string line;

	cin >> n;

	for (int i = 0; i < n; i++) {
		long long num, r = -1;
		bool visited[10] = {false};
		int vcnt = 0, j = 1;

		cin >> num;

		while (num && r == -1) {
			long long tmp = j * num;
			while (tmp) {
				int digit = tmp % 10;
				tmp /= 10;
				if (!visited[digit]) vcnt++;
				visited[digit] = true;
			}
			if (vcnt == 10) r = (j * num);
			j++;
		}

		cout << "Case #" << i + 1 << ": ";
		if (r == -1) cout << "INSOMNIA" << endl;
		else cout << r << endl;
	}

	return 0;
}

