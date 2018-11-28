#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <time.h>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
const int N = 100 + 10;
char str[N];
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int t, cas = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%s", str);
		int cur = str[0] == '+', ans = 0, m = strlen(str);
		for (int i = 1; i < m; ++i)
			if (str[i] != str[i - 1])
				ans++, cur = 1 - cur;
		if (!cur) ans++;
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}