#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; ++i) {
		int a, b, c;
		scanf("%d%d%d", &a,&b,&c);
		printf("Case #%d:", i);
		for (int j=1; j<=a; ++j)
			printf(" %d", j);
		puts("");
	}
	return 0;
}

