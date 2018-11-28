#pragma comment(linker, "/STACK:128777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <deque>
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

#define all(a) a.begin(),a.end()

const int max_n = 4000;

int p[max_n];
int a[max_n];
int b[max_n];

int sb[max_n];

bool g[max_n][max_n];

int st[max_n];

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			p[i] = 0;
			sb[i] = 0;
			st[i] = 0;
			scanf("%d", &a[i]);
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &b[i]);
		}
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (b[i] <= b[j]) {
					g[i][j] = true;
					st[j]++;
				} else {
					g[i][j] = false;
				}
				if (a[i] >= a[j]) {
					g[j][i] = true;
					st[i]++;
				} else {
					g[j][i] = false;
				}
			}
		}
		for (int i = 1; i <= n; i++) {
			int sa = 0;
			int j;
			for (j = 0; j < n; j++) {
				if (p[j]) {
					sa = max(sa, a[j]);
				} else {
					if (st[j] == 0 && sa + 1 == a[j] && sb[j] + 1 == b[j]) {
						break;
					}
				}
			}
			p[j] = i;
			sb[j]++;
			for (int k = 0; k < n; k++) {
				if (g[j][k]) {
					st[k]--;
				}
			}
			for (int k = j - 1; k >= 0; k--) {
				sb[k] = max(sb[k], sb[j]);
			}
		}
		printf("Case #%d:", iTest);
		for (int i = 0; i < n; i++) {
			printf(" %d", p[i]);
		}
		printf("\n");
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}