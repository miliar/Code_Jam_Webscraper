#include <iostream>
#include <stdio.h>

using namespace std;

const int MAXN = 1 << 10;

int n, p[MAXN];

void read() {
	scanf("%d", &n);
	for(int i = 0; i < n; i ++)
		scanf("%d", &p[i]);
}

void solve() {
	int ans = MAXN;
	for(int x = 1; x <= 1000; x ++) {
		int t = 0;
		for(int i = 0; i < n; i ++)
			t += (p[i] / x - (p[i] % x == 0));
		ans = min(ans, t + x);
	}
	
	printf("%d\n", ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int iter = 1; iter <= t; iter ++) {
		printf("Case #%d: ", iter);
		read();
		solve();
	}

    return 0;
}
