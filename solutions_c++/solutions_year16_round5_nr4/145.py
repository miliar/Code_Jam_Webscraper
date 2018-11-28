#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <iostream>

using namespace std;

const int N = 2e5 + 6;

int n, l;
string bad;
set<string> good;

int main() {
	int tests;
	scanf("%d", &tests);
	while (tests--) {
		scanf("%d %d", &n, &l);

		good.clear();
		string s;
		for (int i = 0; i < n; i++) {
			cin >> s;
			good.insert(s);
		}
		cin >> bad;

		static int testCount = 0;
		printf("Case #%d: ", ++testCount);
		if (good.find(bad) != good.end()) {
			puts("IMPOSSIBLE");
		} else {
			for (int i = 0; i < l; i++) {
				printf("0?");
			}
			printf(" 0");
			for (int i = 0; i + 1 < l; i++) {
				printf("1");
			}
			puts("");
		}
	}
	return 0;
}
