#include <cstdio>
#include <algorithm>
using namespace std;

int tn, n, i, j, ret, rd, sd, qt;
double a[1111], b[1111];

int main () {
	scanf("%d", &tn);
	while (tn--) {
		scanf("%d", &n);
		for(i = 1; i <= n; i++) scanf("%lf", &a[i]);
		for(i = 1; i <= n; i++) scanf("%lf", &b[i]);
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		ret = 0;
		for(i = 1; i <= n; i++) {
			sd = 0;
			for(j = n; j >= i; j--) if (a[j] > b[j - i + 1]) ++sd;
			ret = max(ret, sd);
		}
		
		rd = 0; int topb = n, botb = 1;
		for(i = n; i; i--) {
			if (a[i] > b[topb]) {
				++botb;
				++rd;
			} else --topb;
		}
		
		++qt;
		printf("Case #%d: %d %d\n", qt, ret, rd);
	}
	return 0;
}