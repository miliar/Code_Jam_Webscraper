#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for(int ii=1; ii<=t; ii++) {
		printf("Case #%d: ", ii);
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		bool seen[10];
		for (int i=0; i<10; i++) seen[i] = 0;
		int tosee = 10;
		int cur = 0;
		while(tosee) {
			cur += n;
			int x = cur;
			while(x) {
				int d = x % 10;
				if (!seen[d]) { seen[d] = 1; tosee--; }
				x /= 10;
			}
		}
		printf("%d\n", cur);
	}
}
