#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int T, c, i, N, r1, r2, sa, ea, sb, eb;
	double a[1000], b[1000];
	c = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		for (i=0; i<N; i++) scanf("%lf", &a[i]);
		for (i=0; i<N; i++) scanf("%lf", &b[i]);
		sort(a, a+N);
		sort(b, b+N);
		r1 = r2 = 0;
		sa = sb = 0;
		ea = eb = N-1;
		for (i=0; i<N; i++) {
			if (a[ea] > b[eb]) {
				r2++;
				sb++;
				ea--;
			} else {
				ea--;
				eb--;
			}
		}
		sa = sb = 0;
		ea = eb = N-1;
		while (sa < N) {
			if (a[sa] > b[sb]) {
				r1++;
				sa++;
				sb++;
				ea--;
			} else {
				sa++;
			}
		}
		printf("Case #%d: %d %d\n", c++, r1, r2);
	}
	return 0;
}
