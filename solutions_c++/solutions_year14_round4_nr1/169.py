#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

const int maxn = 10000+10;
int n, m;
int a[maxn];
int ans;
int pos;

void work() {
	scanf("%d%d", &n, &m);
	for (int i=0;i<n;i++) {
		scanf("%d", &a[i]);
	}
	sort(a, a + n);
	ans = 0;
	pos = n - 1;
	for (int i=0;i<n;i++) {
		if (a[i] == -1) continue;
		while (a[i] + a[pos] > m && pos > i) pos --;
		if (pos > i) {
			a[pos] = -1;
			pos --;
		}
		ans ++;
	}
	printf("%d\n", ans);
}

int main() {
	int T;
	int cas = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++cas);
		work();
	}
	return 0;
}