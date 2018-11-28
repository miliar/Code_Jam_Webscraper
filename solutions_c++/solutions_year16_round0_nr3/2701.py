#include<stdio.h>

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long tc;
	scanf("%lld", &tc);
	for (long long t = 1; t <= tc;t++) {
		printf("Case #%lld:\n", t);
		long long n, j;
		scanf("%lld%lld", &n, &j);
		long long num = (1 << (n - 1)) | 1;
		while (j != 0) {
			bool flag = false;
			for (long long k = 2; k <= 10; k++) {
				long long sum = 0;
				for (long long i = n - 1; i >= 0; i--) {
					sum *= k;
					if (num&(1 << i)) {
						sum++;
					}
				}
				bool f = false;
				for (long long i = 2; i <= 100; i++) {
					if (sum%i == 0) {
						f = true;
					}
				}
				if (!f) {
					flag = true;
				}
			}
			if (!flag) {
				for (long long i = n - 1; i >= 0; i--) {
					if (num & (1 << i)) {
						printf("1");
					}
					else {
						printf("0");
					}
				}
				printf(" ");
				j--;
				for (long long k = 2; k <= 10; k++) {
					long long sum = 0;
					for (long long i = n - 1; i >= 0; i--) {
						sum *= k;
						if (num&(1 << i)) {
							sum++;
						}
					}
					for (long long i = 2; i <= 100; i++) {
						if (sum%i == 0) {
							printf("%lld ", sum / i);
							break;
						}
					}
				}
				printf("\n");
			}
			num += 2;
		}
	}
}