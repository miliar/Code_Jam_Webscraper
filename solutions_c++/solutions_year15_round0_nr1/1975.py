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

char st[10000];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n;
		scanf("%d %s", &n, &st);
		int s = 0, ans = 0;
		for (int i = 0; i <= n; ++i) {
			int t = st[i] - '0';
			if (s < i) {
				ans += i - s;
				s = i;
			}
			s += t;
		}
		printf("Case #%d: %d\n", o + 1, ans);
	}
	return 0;
}