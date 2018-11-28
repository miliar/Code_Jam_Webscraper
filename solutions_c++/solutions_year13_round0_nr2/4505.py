#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>

#define MAX_SIZE 100

using namespace std;

int n, m;
int a[MAX_SIZE][MAX_SIZE];

bool ok[MAX_SIZE][MAX_SIZE];
bool possible() {
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			ok[i][j] = false;

	int best;

	for (int i = 0; i < n; ++i) {
		best = 0;
		for (int j = 0; j < m; ++j)
			best = max(best, a[i][j]);
		for (int j = 0; j < m; ++j)
			if (a[i][j] == best)
				ok[i][j] = true;
	}

	for (int i = 0; i < m; ++i) {
		best = 0;
		for (int j = 0; j < n; ++j)
			best = max(best, a[j][i]);
		for (int j = 0; j < n; ++j)
			if (a[j][i] == best)
				ok[j][i] = true;
	}

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (!ok[i][j])
				return false;
	return true;
}

int main() {
	int t;
	cin >> t;
	for (int tNow = 1; tNow <= t; ++tNow) {
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> a[i][j];
		cout << "Case #" << tNow << ": ";
		cout << (possible() ? "YES" : "NO") << endl;
	}
	return 0;
}
