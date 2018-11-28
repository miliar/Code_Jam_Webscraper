#include <cstdio>
#include <map>
#include <set>
int main(void) {
	int t;
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		printf("Case #%d:", i);
		for (int i = 1; i <= a; i++) {
			printf(" %d", i);
		}
		printf("\n");
	}
}