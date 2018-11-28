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
#define taskname "task_b"
const ldb pi = acos(-1.0);
const double inf = (double) 1e18;
const int M = (int) 1e6;

int main() {
	assert(freopen(taskname".in", "r", stdin));
	assert(freopen(taskname".out", "w", stdout));
	int t;
	double c, f, x, cur, ans, v;
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%lf%lf%lf", &c, &f, &x);
		v = 2, ans = inf, cur = 0;
		for (int i = 0; i <= M; ++i) {
			ans = min(ans, cur + x / v);
			cur += c / v, v += f;
		}
		printf("Case #%d: %.10lf\n", it + 1, ans);
	}
	return 0;
}