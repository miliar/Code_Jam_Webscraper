#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <algorithm>
using namespace std;

typedef long long ll;
const int N = 111111;
int a[N];
int n, m;

int main() {
	int _, cas = 0;
	scanf("%d", &_);
	while (_--) {
		scanf("%d%d", &n, &m);
		for (int i=0; i<n; ++i) {
			scanf("%d", &a[i]);
		}
		sort(a, a+n);
		int head = 0, ans = 0;
		for (int i=n-1; i>=head; --i) {
			if (i != head && a[i] + a[head] <= m) {
				++ head;
			}
			++ ans;
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}