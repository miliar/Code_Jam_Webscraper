#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <cctype>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

#define FILE_IN  "D-small-attempt0.in"
#define FILE_OUT "D-small-attempt0.out"

int n;
double mem[1 << 20];

double get(int plan) {
	double &res = mem[plan];
	if (res >= 0)
		return res;
	res = 0.0;
	for (int i = 0; i < n; ++i) if (!(plan & (1 << i))) {
		int x = 0;
		for (int j = (i - 1 + n) % n; (plan & (1 << j)); j = (j - 1 + n) % n)
			x += 1;
		int nplan = plan | (1 << i);
		res += ((n - x / 2.0) + get(nplan)) * (x + 1) / n;
	}
	return res;
}

void solve() {
	fill(mem, mem + (1 << 20), -1);
	char splan[22];
	scanf("%s", splan);
	n = strlen(splan);
	int plan = 0;
	for (int i = 0; i < n; ++i)
		if (splan[i] == 'X')
			plan |= 1 << i;
	double res = get(plan);
	printf("%.9lf\n", res);
}

int main() {
	freopen(FILE_IN, "r", stdin);
	freopen(FILE_OUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: ", i);
		fprintf(stderr, "Case #%d: ...", i); fflush(stderr);
		solve();
		fprintf(stderr, " done\n"); fflush(stderr);
	}
	return 0;
}
