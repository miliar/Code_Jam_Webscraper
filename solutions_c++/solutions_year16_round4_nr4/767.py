#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(int i=a; i<=b; i++)
#define fj(a, b) for(int j=a; j<=b; j++)
#define fo(a, b) for(int o=a; o<=b; o++)
#define fdi(a, b) for(int i=a; i>=b; i--)
#define fdj(a, b) for(int j=a; j>=b; j--)
#define fdo(a, b) for(int o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

int number_of_tests;
int test_number;

#define MAX 20

int n;
int matr[MAX][MAX];

void read() {
	scanf("%d", &n);
	fj(1, n) {
		char str[MAX];
		scanf("%s", str + 1);
		fi(1, n) {
			matr[j][i] = str[i] == '1';
		}
	}
}

int p[MAX];
int C;

int f[MAX][20];
int d[MAX][20];
int ans;

int fun2(int x, int mask) {
	if (x > n) return 1;
	if (f[x][mask] == C) return d[x][mask];
	int res = 1;

	int g = 0;

	fi(1, n) {
		if ((1 << i) & mask) continue;
		if (matr[p[x]][i]) {
			g = 1;
			if (!fun2(x + 1, mask | (1 << i))) {
				res = 0;
			}
		}
	}

	if (!g) res = 0;

	f[x][mask] = C;
	return d[x][mask] = res;
}

bool check() {
	fi(1, n) {
		p[i] = i;
	}
	do {
		C++;
		if (!fun2(1, 0)) return false;
	} while (next_permutation(p + 1, p + n + 1));
	return true;
}

int cur;

void fun(int x, int y) {
	if (cur >= ans) return;
	if (x > n) {
		x = 1;
		y++;
		if (y > n) {
			if (check()) {
				ans = cur;
				check();
			}
			return;
		}
	}
	if (matr[y][x] == 0) {
		matr[y][x] = 1;
		cur++;
		fun(x + 1, y);
		cur--;
		matr[y][x] = 0;
	}
	fun(x + 1, y);
}

void solve() {
	cur = 0;
	ans = 1000000000;
	fun(1, 1);
	printf("%d\n", ans);
}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt","r",stdin);
	} else {
		freopen(argv[1], "r",stdin);
	}
	freopen("output.txt","w",stdout);
	scanf("%d", &number_of_tests);
	for (test_number = 1; test_number <= number_of_tests; test_number++) {
		read();
		printf("Case #%d: ", test_number);
		solve();
		fflush(stdout);
	}
	return 0;
}
