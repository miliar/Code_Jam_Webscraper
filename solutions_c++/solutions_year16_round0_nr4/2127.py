#include <stdio.h>

long long pow(int b, int e) {
	long long ans = 1;
	for (int i = 0; i < e; i++) ans *= b;
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++) {
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d:", tt+1);
		if (((k-1)/c+1)>s) printf(" IMPOSSIBLE\n");
		else {
			for (int i = 0; i < k;) {
				long long base = pow(k, c);
				long long pos = 0;
				for (int j = 0; j < c; j++) {
					if (i == k) break;
					base /= k;
					pos += base * i++;
				}
				printf(" %lld", pos+1);
			}
			printf("\n");
		}
	}
}
