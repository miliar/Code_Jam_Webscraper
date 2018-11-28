#define _CRT_SECURE_NO_DEPRICATE
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <list>

#define FOR(i, p, n) for(int i = p; i < n; ++i)
#define FORD(i, p, n) for(int i = p; i >= n; --i)
#define F first
#define S second
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;

string str;

long long st[11][17];
int n, k;

long long check_num(long long tmp) {
	for (long long i = 2; i * i <= tmp; ++i) if (tmp % i == 0) return i;
	return 0;
}


long long get_num(long long num, int s) {
	long long res = 0;
	int i = 0;
	while (num) {
		res += (num & 1) * st[s][i];
		num >>= 1;
		++i;
	}
	return res;
}

bool try_num(long long num) {
	long long tmp;
	long long div[11];
	FOR(j, 2, 11) {
		tmp = get_num(num, j);
		div[j] = check_num(tmp);
		if (!div[j]) return 0;
	}
	printf("%I64d ", get_num(num, 10));
	FOR(j, 2, 11) printf("%I64d ", div[j]);
	printf("\n");
}

int main() {
	FOR(i, 2, 11) st[i][0] = 1;
	FOR(j, 2, 11) FOR(i, 1, 17) st[j][i] = j * st[j][i - 1];
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		cin >> n >> k;
		printf("Case #%d:\n", i + 1);
		for (int j = st[2][0] + st[2][n - 1]; k && j < st[2][n]; j += 2) if (try_num(j)) --k;
	}
	cin >> n;

	return 0;
}