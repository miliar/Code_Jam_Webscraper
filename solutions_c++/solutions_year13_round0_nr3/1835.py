#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <vector>

#define ll long long


#define TASK_NAME "input"
#define MAXN int(1e4)

using namespace std;

ll is_pali(ll x) {
	ll _x = x, xRev = 0;
	while (_x > 0) {
		xRev = (xRev * 10) + (_x % 10);
		_x /= 10;
	}
	return xRev == x;
}

int cnt;
ll baseX[100000];
ll maxC = (ll)1e14 + 100;

int get(ll r) {
	int have = 0;
	while (have < cnt && baseX[have] <= r) {
		have++;
	}
	return have;
}
    
int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);

	for (ll x = 1; x * x <= maxC; x++) {
		if (is_pali(x) && is_pali(x * x)) {
			cerr << x << endl;
			baseX[cnt++] = x * x;
		}
	}

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		ll a, b;
		scanf("%I64d %I64d", &a, &b);
		printf("Case #%d: %d\n", i + 1, get(b) - get(a - 1)); 
	}
	
	return 0;
}
