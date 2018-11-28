#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

int a[1000];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n;
		scanf("%d", &n);
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			ans = max(ans, a[i]);
		}
		for (int i = 1; i < ans; ++i) {
			int s = 0;
			for (int j = 0; j < n; ++j) 
				if (a[j] > i) s += (a[j] - 1) / i;
			ans = min(ans, i + s);
		}
		printf("Case #%d: %d\n", o + 1, ans);
	}
	return 0;
}