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
#include <cassert>
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

#define MAX 100

int n, m;
int k;
int p[2 * (MAX + MAX)];

void read() {
	scanf("%d %d", &m, &n);
	k = 2 * (n + m);
	fi(1, k) {
		scanf("%d", &p[i]);
	}
}

char matr[MAX][MAX];
char ans[MAX][MAX];
int e[MAX];

int C;
int color[MAX][MAX];
map <pair<int, int>, int> num;

set <int> nums;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

bool field(int x, int y) {
	if (x < 0 || x >= 2 * n) return false;
	if (y < 0 || y >= 2 * m) return false;
	return true;
}

void dfs(int x, int y) {
	if (num.find(mp(y, x)) != num.end()) {
		nums.insert(num[mp(y, x)]);
	}
	if (!field(x, y)) return;
	if (matr[y][x] == '#') return;
	if (color[y][x] == C) return;
	color[y][x] = C;
	int x2, y2;
	fi(0, 3) {
		x2 = x + dx[i];
		y2 = y + dy[i];
		dfs(x2, y2);
	}

	if ((x + y) % 2 == 0) {
		dfs(x + 1, y - 1);
		dfs(x - 1, y + 1);
	} else {
		dfs(x - 1, y - 1);
		dfs(x + 1, y + 1);
	}
}

bool check() {
	C++;
	fj(0, 2 * m - 1) {
		fi(0, 2 * n - 1) {
			nums.clear();
			dfs(i, j);
			if (nums.size() == 2) {
				if (e[*nums.begin()] != *nums.rbegin()) {
					return false;
				}
			}
			assert(nums.size() == 0 || nums.size() == 2);
		}
	}
	return true;
}

int fun(int x, int y) {
	if (x == n) {
		x = 0;
		y++;
		if (y == m) {
			if (check()) return true;
			return false;
		}
	}
	ans[y][x] = '/';
	matr[2 * y][2 * x] = '.'; matr[2 * y][2 * x + 1] = '#';
	matr[2 * y + 1][2 * x] = '#'; matr[2 * y + 1][2 * x + 1] = '.';
	if (fun(x + 1, y)) return true;
	ans[y][x] = '\\';
	matr[2 * y][2 * x] = '#'; matr[2 * y][2 * x + 1] = '.';
	matr[2 * y + 1][2 * x] = '.'; matr[2 * y + 1][2 * x + 1] = '#';
	if (fun(x + 1, y)) return true;
	return false;
}

void solve() {
	ZERO(matr);
	ZERO(e);
	num.clear();
	for (int i = 1; i <= k; i += 2) {
		e[p[i]] = p[i + 1];
		e[p[i + 1]] = p[i];
	}

	int q = 0;
	for (int i = 0; i < 2 * n; i += 2) {
		q++;
		num[mp(-1, i)] = q;
		num[mp(-1, i + 1)] = q;
	}
	for (int j = 0; j < 2 * m; j += 2) {
		q++;
		num[mp(j, 2 * n)] = q;
		num[mp(j + 1, 2 * n)] = q;
	}
	for (int i = 2 * n - 1; i >= 0; i -= 2) {
		q++;
		num[mp(2 * m, i)] = q;
		num[mp(2 * m, i - 1)] = q;
	}
	for (int j = 2 * m - 1; j >= 0; j -= 2) {
		q++;
		num[mp(j, -1)] = q;
		num[mp(j - 1, -1)] = q;
	}
	printf("\n");
	if (fun(0, 0)) {
		fj(0, m - 1) {
			fi(0, n - 1) {
				printf("%c", ans[j][i]);
			}
			printf("\n");
		}
	} else {
		printf("IMPOSSIBLE\n");
	}
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
