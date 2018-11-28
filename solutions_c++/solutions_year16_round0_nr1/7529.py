#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t, n;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		if (!n) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		bool digits[10] = { false };
		int cnt = 0;
		for (int j = 1; true; ++j) {
			int x = n * j;
			while (true) {
				int d = x % 10;
				if (!digits[d]) {
					digits[d] = true;
					++cnt;
				}
				x /= 10;
				if (!x)
					break;
			}
			if (cnt == 10) {
				printf("Case #%d: %d\n", i, n * j);
				break;
			}
		}
	}
	
	return 0;
}