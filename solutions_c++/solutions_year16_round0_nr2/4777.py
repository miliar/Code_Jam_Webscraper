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

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int n, res;
	bool cur;
	cin >> n;
	FOR(i, 0, n) {
		cin >> str;
		res = 0;
		cur = (str[0] == '+' ? 1 : 0);
		FOR(i, 1, str.length()) {
			if (str[i] == '+' && !cur) {
				++res;
				cur = 1;
			}
			else if (str[i] == '-' && cur) {
				++res;
				cur = 0;
			}
		}
		if (!cur) ++res;
		printf("Case #%d: %d\n", i + 1, res);
	}
	cin >> n;

	return 0;
}