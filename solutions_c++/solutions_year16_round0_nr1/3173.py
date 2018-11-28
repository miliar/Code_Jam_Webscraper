#include<stdio.h>


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int TC = 1; TC <= tc;TC++) {
		
		long long n;
		scanf("%lld", &n);
		if (n==0) {
			printf("Case #%d: INSOMNIA\n", TC);
			continue;
		}
		bool chk[10] = { 0, };
		int cnt = 0;
		for (int i = 1;; i++) {
			long long temp = n*i;
			while (temp != 0) {
				if (!chk[temp % 10]) {
					chk[temp % 10] = true;
					cnt++;
				}
				temp /= 10;
			}
			if (cnt == 10) {
				printf("Case #%d: %lld\n", TC, n*i);
				break;
			}
		}
		
	}
}
