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

bool nums[10];

bool sol(int a) {
	while (a) {
		nums[a % 10] = 1;
		a /= 10;
	}
	FOR(i, 0, 10) if (!nums[i]) return 1;
	return 0;
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int n, a;
	cin >> n;
	FOR(i, 0, n) {
		FOR(j, 0, 10) nums[j] = 0;
		scanf("%d", &a);
		if (!a) {
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		int k = a;
		while (sol(k)) k += a;
		printf("Case #%d: %d\n", i + 1, k);
	}

	return 0;
}