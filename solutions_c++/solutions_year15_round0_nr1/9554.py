#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <climits>
using namespace std;

char str[1010];
int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int ans = 0;
		int n;
		scanf("%d", &n);
		scanf("%s", str);
		int have = str[0] - '0';
		for (int i = 1; i <= n; i++) {
			if (have < i) {
				ans += i - have;
				have = i;
			}
			have += str[i] - '0';
		}
		printf("Case #%d: %d\n", cas, ans);
	}
    return 0;
}