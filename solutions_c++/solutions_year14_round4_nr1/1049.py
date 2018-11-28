#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int n, x;
int a[20000];
bool f[20000];

void work() {
	scanf("%d%d", &n, &x);
	for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
	sort(a, a + n);
	int ans = n;
	int l = 0, r = n - 1;
	while (l < r) {
		if (a[l] + a[r] <= x) {
			--ans;
			++l; --r;
		} else {
			--r;
		}
	}
	printf("%d\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		work();
	}
	return 0;
}
