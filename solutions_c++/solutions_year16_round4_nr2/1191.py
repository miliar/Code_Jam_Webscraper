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

//#define MAX 230
#define MAX 20

int n, k;
double p[MAX];

void read() {
	ZERO(p);
	scanf("%d %d", &n, &k);
	fi(1, n) {
		scanf("%lf", &p[i]);
	}
}

double d[MAX][MAX][MAX];
int f[MAX][MAX][MAX];

double fun(int x, int q, int t) {
	if (x == 0) {
		if (q == 0 && t == 0) return 1;
		return 0;
	}
	if (t < 0) return 0;
	if (q > x) return 0;
	if (f[x][q][t]) return d[x][q][t];
	double res = 0;		

	res = max(res, fun(x - 1, q, t));
	res = max(res, fun(x - 1, q - 1, t - 1) * p[x] + fun(x - 1, q - 1, t) * (1 - p[x]));

	f[x][q][t] = 1;
	return d[x][q][t] = res;
}

int bits(int x) {
	int res = 0;
	while (x) {
		res += x & 1;
		x >>= 1;
	}
	return res;
}

void solve() {
	double best = 0;

	double p0[MAX];
	COPY(p0, p);

	fi(0, (1 << n) - 1) {
		if (bits(i) != k) continue;
		int q = 0;
		fj(0, n) {
			if ((1 << j) & i) {
				q++;
				p[q] = p0[j + 1];
			}
		}
		ZERO(d);
		ZERO(f);
		best = max(best, fun(k, k, k / 2));
	}

	printf("%.9lf\n", best);
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
