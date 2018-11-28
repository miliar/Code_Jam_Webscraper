#pragma comment(linker, "/STACK:100000000")
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;
#define int64 long long
#define ldb long double
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define taskname "task_a"
const ldb pi = acos(-1.0);
const int max_it = 100;
const int N = (int) 1e6 + 10;
int a[N], mx, t, n, p, q, r, s;
int64 sum;

bool check(int64 x) {
	int m = 1;
	int64 sum = 0;
	for (int i = 0; i < n; ++i) {
		if (sum + a[i] > x) {
			m++;
			sum = 0;
		}
		sum += a[i];
	}
	return (m <= 3);
}

int main() {
	assert(freopen(taskname".in", "r", stdin));
	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d%d%d%d%d", &n, &p, &q, &r, &s), sum = 0, mx = 0;
		for (int i = 0; i < n; ++i) {
			a[i] = ((i * (int64) p + q) % r + s);
			sum += a[i], mx = max(mx, a[i]);
		}
		int64 l = mx, r = sum;
		while (l < r) {
			int64 q = (l + r) / 2;
			if (check(q)) r = q;
			else l = q + 1;
		}
		printf("Case #%d: %.10Lf\n", it + 1, (ldb) (sum - l) / sum);
	}
	return 0;
}

