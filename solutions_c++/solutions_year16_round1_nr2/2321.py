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

#define MAX 60

int n;
int v[MAX][MAX];

void read() {
	ZERO(v);
	scanf("%d", &n);
	fi(1, 2 * n - 1) {
		fj(1, n) {
			int x;
			scanf("%d", &x);
			v[i][j] = x;
		}
	}
	fj(1, 2 * n - 1) {
		fi(1, 2 * n - 2) {
			int f = 0;
			fo(1, n) {
				if (v[i][o] > v[i + 1][o]) {
					f = 1;
					break;
				} else if (v[i][o] < v[i + 1][o]) {
					f = 0;
					break;
				}
			}
			if (f) {
				fo(1, n) {
					swap(v[i][o], v[i + 1][o]);
				}
			}
		}
	}
}

int matr[MAX][MAX];

bool try_hor(int y, int c) {
	fi(1, n) {
		if (matr[y][i] != 0 && matr[y][i] != v[c][i]) return false;
	}
	return true;
}

bool try_ver(int x, int c) {
	fj(1, n) {
		if (matr[j][x] != 0 && matr[j][x] != v[c][j]) return false;
	}
	return true;
}

vector <pair<int, int> > fill_hor(int y, int c) {
	vector <pair<int, int> > res;
	fi(1, n) {
		if (matr[y][i] == 0) {
			matr[y][i] = v[c][i];
			res.pb(mp(i, y));
		}
	}
	return res;
}

vector <pair<int, int> > fill_ver(int x, int c) {
	vector <pair<int, int> > res;
	fj(1, n) {
		if (matr[j][x] == 0) {
			matr[j][x] = v[c][j];
			res.pb(mp(x, j));
		}
	}
	return res;
}

int ans[MAX];
bool ans_found;
int used_v[MAX];
int used_h[MAX];

void fun(int x, int y, int c, bool f = false) {
	if (ans_found) return;
	if (c == 2 * n) {
		int p = 0;
		fj(1, n) {
			if (used_h[j] == 0) {
				fi(1, n) {
					p++;
					ans[p] = matr[j][i];
				}
			}
		}

		fi(1, n) {
			if (used_v[i] == 0) {
				fj(1, n) {
					p++;
					ans[p] = matr[j][i];
				}
			}
		}
		ans_found = true;
		return;
	}
	if (y <= n && v[c][1] > matr[y - 1][1] && try_hor(y, c)) {
		vector <pair<int, int> > to_remove = fill_hor(y, c);
		used_h[y] = 1;
		fun(x, y + 1, c + 1, f);
		used_h[y] = 0;
		fi(0, SIZE(to_remove) - 1) {
			matr[to_remove[i].second][to_remove[i].first] = 0;
		}
	}

	if (x <= n && v[c][1] > matr[1][x - 1] && try_ver(x, c)) {
		vector <pair<int, int> > to_remove = fill_ver(x, c);
		used_v[x] = 1;
		fun(x + 1, y, c + 1, f);
		used_v[x] = 0;
		fi(0, SIZE(to_remove) - 1) {
			matr[to_remove[i].second][to_remove[i].first] = 0;
		}
	}

	if (!f) {
		if (y <= n) {
			fun(x, y + 1, c, 1);
		}
		if (x <= n) {
			fun(x + 1, y, c, 1);
		}
	}
}

void solve() {
	ans_found = false;
	ZERO(ans);
	fun(1, 1, 1);
	fi(1, n) {
		printf("%d ", ans[i]);
	}
	printf("\n");
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
