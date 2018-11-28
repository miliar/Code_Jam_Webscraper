#include <stdio.h>
#include <algorithm>

int m[10001];
int main(void)
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int n;
		scanf("%d", &n);
		for (int i=0; i<n; i++) {
			scanf("%d", &m[i]);
		}
		int sum = 0;
		int mx = 0;
		for (int i=0; i<n-1; i++) {
			int d = m[i] - m[i+1];
			sum += std::max(0, d);
			mx = std::max(mx, d);
		}
		int eat = 0;
		for (int i=0; i<n-1; i++) {
			eat += std::min(mx, m[i]);
		}
		printf("Case #%d: %d %d\n", t, sum, eat);
	}
	return 0;
}
