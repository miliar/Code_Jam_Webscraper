#pragma comment(linker, "/STACK:128777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>

typedef long long i64;
typedef unsigned int u32;
const int null = 0;

using namespace std;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0? -a: a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

int a[100][100];
int row[100], col[100];

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		printf("Case #%d: ", iTest);
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			row[i] = 0;
		}
		for (int j = 0; j < m; j++) {
			col[j] = 0;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &a[i][j]);
				row[i] = max(row[i], a[i][j]);
				col[j] = max(col[j], a[i][j]);
			}
		}
		bool good = true;
		for (int i = 0; good && i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (min(row[i], col[j]) != a[i][j]) {
					good = false;
					break;
				}
			}
		}
		if (good) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}