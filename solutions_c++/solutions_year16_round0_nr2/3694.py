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
	getline(cin, line);

	for (int i = 0; i < n; i++) {
		int r = 0, hvisited = 0, bvisited = 0;

		getline(cin, line);

		for (int j = 0; j < line.length(); j++) {
			char ch = line[j];
			if (ch == '-') {
				if (hvisited) {
					r++;
					hvisited = 0;
				}
				
				bvisited = 1;
			} else if (ch == '+') {
				if (bvisited) {
					r++;
					bvisited = 0;
				}
				hvisited = 1;
			}
		}

		if (bvisited) r++;
		
		cout << "Case #" << i + 1 << ": " << r << endl;
	}

	return 0;
}

