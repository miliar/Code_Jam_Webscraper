#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 4)
using namespace std;

int e, r, n;
int v[MAXN];

int go(int pos, int curEnergy) {
	if (pos == n) {
		return 0;
	}
	
	int ans = 0;
	
	for (int i=0; i <= curEnergy; ++i)
		ans = max(ans, go(pos+1, min(e, curEnergy-i+r)) + i*v[pos]);
	
	return ans;
}

inline void solve(int test) {
	printf("Case #%d: %d\n", test, go(0, e));	
}

inline void read() {
	scanf("%d%d%d", &e, &r, &n);
	for (int i=0; i < n; ++i)
		scanf("%d", &v[i]);
}

int main() {
	int brt = 0, test = 0;
	scanf("%d", &brt);
	
	while (brt --) {
		read();
		solve(++test);
	}
	return 0;
}