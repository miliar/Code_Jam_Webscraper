#include <cstdio>
#include <iostream>

#pragma warning(disable:4996)

using namespace std;

int t;
long long n,rlt;

long long sol(long long k) {
	if (k == k*2)
		return -1;
	else {
		long long tmp;
		int flagsum = 0, i = 0, flag[10] = { 0 };
		do {
			i++;
			tmp = i*k;
			while (tmp > 0) {
				int rem = tmp % 10;
				tmp = tmp / 10;
				if (flag[rem] == 0) {
					flag[rem] = 1;
					flagsum += 1 << rem;
				}
			}
		} while (flagsum != 1023);
		return  (i*k);
	}
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%lld", &n);
		rlt = sol(n);

		printf("Case #%d: ", i);
		if (rlt == -1) {
			printf("INSOMNIA");
		}
		else {
			printf("%lld", rlt);
		}
		printf("\n");
	}
	return 0;
}
