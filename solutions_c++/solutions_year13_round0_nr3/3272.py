#include <stdio.h>
#include <math.h>
int num[6] = {
	1,4,9,121,484,
};
int main() {
	int t;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for(int k = 1; k <= t; k++) {
		int n, m;
		scanf("%d%d", &n, &m);
		printf("Case #%d: ", k);
		int count = 0;
		for(int i = 0; i <= 4; i++) if(num[i] >= n && num[i] <= m) count++;
		printf("%d\n", count);
	}
}