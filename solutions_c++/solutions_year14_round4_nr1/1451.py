#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 10000 + 10;

int a[N];

int main() {
	int t;
	scanf("%d", &t);

	for(int kase = 1; kase <= t; kase++) {
		int n, x;
		scanf("%d%d", &n, &x);

		for(int i = 0; i < n; i++)	scanf("%d", &a[i]);

		sort(a, a + n);

		int ans = 0, l = 0, r = n-1;
		while(l <= r) {
			if(a[l] + a[r] <= x)	l++;
			r--;
			ans++;
		}

		printf("Case #%d: %d\n", kase, ans);
	}

	return 0;
}
