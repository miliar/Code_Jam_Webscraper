#include <iostream>
#include <algorithm>
using namespace std;

const int N = 1003;
int a[N];

int getMinutes(int n, int upLimit) {
	int minutes = 0;
	for (int i = 0; i < n; i++) {
		minutes += (a[i]-1)/upLimit;
	}
	return minutes;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		int n;
		scanf("%d", &n);

		int maxx = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", a+i);
			maxx = max(a[i], maxx);
		}

		int minn = 0x3fffffff;
		for (int i = 1; i <= maxx; i++) {
			if (i >= minn) break;
			int minutes = i+getMinutes(n, i);
			minn = min(minutes, minn);
		}
		printf("Case #%d: %d\n", cas, minn);
	}
	return 0;
}


