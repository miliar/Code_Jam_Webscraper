#include <iostream>
#include <algorithm>
using namespace std;

int tn, ti, n, k, ans, i, a[10000 + 5], j;

int main (int argc, char * const argv[]) {
	scanf("%d", &tn);
	for(ti = 1; ti <= tn; ti++) {
		ans = 0;
		scanf("%d %d", &n, &k);
		for(i = 1; i <= n; i++) scanf("%d", &a[i]);
		sort(a + 1, a + n + 1);
		reverse(a + 1, a + n + 1);
		for(i = 1; i <= n; i++) if (a[i] > 0){
			a[i] *= -1;
			for(j = i + 1; j <= n; j++) if (a[j] > 0 && -a[i] + a[j] <= k) {
				a[j] *= -1;
				break;
			}
			++ans;
		}
		printf("Case #%d: %d\n", ti, ans);
	}
    return 0;
}
