#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

int st[103];

bool all_ones(int l) {
	for (int i = 0; i < l; ++i)
		if (st[i] != 1) return false;
	return true;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		string s;
		cin >> s;
		for (int i = 0; i < (int)s.size(); ++i)
			st[i] = s[i] == '+' ? 1 : 0;

		int l = (int)s.size();
		if (all_ones(l)) {
			printf("Case #%d: 0\n", t);
			continue;
		}
		int bot = l - 1;
		for (;; --bot) if (st[bot] == 0) break;
		int top = 0;
		int cost = 0;
		while (st[top] == 1) ++top;
		if (top > 0) ++cost;
		for (;;) {
			while (top <= bot && st[top] == 0) ++top;
			if (top > bot) {
				++cost;
				break;
			}
			while (top <= bot && st[top] == 1) ++top;
			cost += 2;
		}
		printf("Case #%d: %d\n", t, cost);
	}
	return 0;
}