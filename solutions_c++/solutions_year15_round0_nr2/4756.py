#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;
int p[1024];
int main() {
	int testnum, D, l, r, mid, total;
	bool suc;
	scanf("%d", &testnum);
	for (int test = 1;test <= testnum;test++) {
		scanf("%d", &D);
		l = r = 1;
		for (int i = 0;i < D;i++) {
			scanf("%d", &p[i]);
			r = max(r, p[i]);
		}
		sort(p, p + D);
		while (l < r) {
			mid = (l + r) >> 1;
			suc = false;
			for (int i = 1;!suc && i <= mid;i++) {
				total = i;
				for (int j = 0;total <= mid && j < D;j++) {
					total += (p[j] - 1) / i;
				}
				if (total <= mid)
					suc = true;
			}
			if (suc)
				r = mid;
			else
				l = mid + 1;
		}
		printf("Case #%d: %d\n", test, l);
	}
	return 0;
}
