#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;

typedef long long ll;
const int N = 111111;
int a[N], c[N], b[N];
int n, ans;

void work(int l, int r) {
	if (l < r) {
		while (l < r) {
			swap(a[l], a[l+1]);
			++l;
			++ans;
		}
	} else {
		while (l > r) {
			swap(a[l], a[l-1]);
			--l;
			++ans;
		}
	}
}

int main() {
	int _, cas = 0;
	scanf("%d", &_);
	while (_--) {
		scanf("%d", &n);
		for (int i=0; i<n; ++i) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b, b+n);

		int l = 0, r = n - 1;
		ans = 0;
		for (int i=0; i<n; ++i) {
			int id = -1;
			for (int j=0; j<n; ++j) {
				if (a[j] == b[i]) {
					id = j;
					break;
				}
			}
			int pl = abs(id - l);
			int pr = abs(id - r);

			if (pl < pr) {
				work(id, l);
				l ++;
			} else {
				work(id, r);
				r --;
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}