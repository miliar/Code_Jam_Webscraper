#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldb;

int cnt[1001], T, smax;
string ans[] = { "RICHARD", "GABRIEL" };
int answers[101];
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cin >> T;
	int x, r, c;
	
	for (int tc = 1; tc <= T; tc++) {
		cin >> x >> r >> c;
		if (r > c) swap(r, c);
		if (x == 1) {
			answers[tc] = 1;
			continue;
		}
		if (x == 2) {
			if (r * c % 2 == 0)	answers[tc] = 1;
			continue;
		}
		if (x == 3) {
			if (r == 2 && c == 3 || r == 3)	answers[tc] = 1;
			continue;
		}
		if (r == 3 && c == 4 || r == 4)	answers[tc] = 1;
	}
	for (int tc = 1; tc <= T; tc++)
		printf("Case #%d: %s\n", tc, ans[answers[tc]].c_str());

	return 0;
}