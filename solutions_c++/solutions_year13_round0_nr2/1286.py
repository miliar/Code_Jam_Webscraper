#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

void InitFiles() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

const int MAXN = 100;

int a[MAXN][MAXN];
int n, m;

bool Ok(int x, int y) {
	bool okVert = true;
	for (int j = 0; j < m; ++j) {
		if (a[x][j] > a[x][y]) {
			okVert = false;
			break;
		}
	}

	bool okHor = true;
	for (int i = 0; i < n; ++i) {
		if (a[i][y] > a[x][y]) {
			okHor = false;
			break;
		}
	}
	return okVert || okHor;
}

string Solve() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			scanf("%d", &a[i][j]);
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (!Ok(i, j)) {
				return "NO";
			}
		}
	}
	return "YES";
}

int main()
{
	InitFiles();

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: %s\n", i + 1, Solve().c_str());
	}
	return 0;
}