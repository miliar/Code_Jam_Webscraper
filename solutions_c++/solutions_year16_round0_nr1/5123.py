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
void calc(int &vis,ll k){
	while (k) {
		vis |= (1 << (k % 10));
		k /= 10;
	}
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

#endif
	int target = (1 << 10) - 1;
	int t, n, ans, vis,cas=1;
	ll k;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		if (!n) {
			printf("Case #%d: INSOMNIA\n",cas++);
			continue;
		}
		k = ans = vis = 0;
		while (vis != target) {
			k += n;
			calc(vis, k);
			ans++;
		}
		printf("Case #%d: %lld\n", cas++, k);
	}
	return 0;
}