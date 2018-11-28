#pragma comment(linker, "/STACK:836777216")

#define INF (long long)1e18
#define EPS 1e-15
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <memory.h>

using namespace std;

int tests;
long long p, q;

long long gcd(long long a, long long b) {
	if (b == 0ll)
		return a;
	else
		return gcd(b, a % b);
}

bool check(long long pp, long long qq) {
	if ((pp == 0 || pp == 1) && qq == 1) return true;
	bool re = true;
	int ind = 0;
	while (2 * pp < qq) {
		if (qq % 2 != 0) {
			re = false;
			break;
		}
		qq = qq / 2;
		ind ++;
	}
	if (qq % 2 != 0) re = false;
	if (!re) return false;
	else return check(pp - qq / 2, qq / 2);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		scanf("%lld/%lld", &p, &q);
		long long r = gcd(p, q);
		p /= r, q /= r;
		int ind = 0;
		int f = 1;
		while (2 * p < q) {
			if (q % 2 != 0) {
				f = 0;
				break;
			}
			p = p;
			q = q / 2;
			ind ++;
		}
		bool ans = check(p - q / 2, q / 2);
		if (q % 2 == 0 && f && ans) {
			printf("Case #%d: %d\n", test, ind + 1, p - q / 2, q / 2);
		} else {
			printf("Case #%d: impossible\n", test);
		}
	}
	return 0;
}