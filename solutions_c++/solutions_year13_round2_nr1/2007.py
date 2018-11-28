#include <cstdio>
#include <cstring>
#include <set>
#include <algorithm>
using namespace std;
const int MAXN = 1000010;
int mote[MAXN];
int main() {
	int testnum, ans, cur, a, n;
	scanf("%d", &testnum);
	for (int test = 1;test <= testnum;test++) {
		scanf("%d%d", &a, &n);
		for (int i = 0;i < n;i++) {
			scanf("%d", &mote[i]);
		}
		if (a == 1) {
			printf("Case #%d: %d\n", test, n);
			continue;
		}
		sort(mote, mote + n);
		ans = n;
		cur = 0;
		for (int i = 0;i < n;i++) {
			if (a <= mote[i]) {
				ans = min(ans, cur + n - i);
				while (a <= mote[i]) {
					a <<= 1;
					a--;
					cur++;
				}
			}
			a += mote[i];
		}
		ans = min(ans, cur);
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
