#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int n;

struct node {
	int x, t;
} a[2000];

bool cmp(const node &t1, const node &t2) {
	return (t1.x < t2.x);
}

void work() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &a[i].x);
		a[i].t = i;
	}
	sort(a, a + n, cmp);
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		int tmp = 0;
		for (int j = i + 1; j < n; ++j)
			if (a[j].t > a[i].t) ++tmp;
		ans += min(tmp, n - i - 1 - tmp);
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
