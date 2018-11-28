#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

int a[2000];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int res = 0;
		int M;
		int s = 0;
		scanf("%d", &M);
		for (int i=0; i<=M; i++) {
			char c[2] = {};
			scanf(" %c", &c[0]);
			int a = atoi(c);
			if (a > 0) {
				int b = std::max(i-s, 0);
				s += b;
				res += b;
			}
			s += a;
		}
		printf("Case #%d: %d\n", t, res);
	}
}