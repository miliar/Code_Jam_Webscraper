#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

long long trans(int val, int base)
{
	vector<int> vt;
	
	while (true) {
		vt.push_back(val % 2 == 1 ? 1 : 0);
		val = val >> 1;
		if (val == 0) break;
	}

	long long res = 0;
	for (int i = vt.size() -1; i >= 0; i--) {
		res += vt[i];
		res *= base;
	}
	res /= base;

	return res;
}

long long find_divisor(long long val)
{
	for (long long i = 2; i < val; i++) {
		if (i * i > val)
			break;

		if (val % i == 0)
			return i;
	}

	return -1;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int w = 0; w < T; w++) {
		int N, J;
		scanf("%d %d", &N, &J);

		printf("Case #1:\n");
		long long base = 1 << (N - 1);
		base += 1;

		int cnt = 0;

		// generate candidate jamcoin
		long long can = 1 << (N - 2);
		for (long long i = 0; i < can; i++) {
			long long val = base + (i * 2);

			long long values[11];
			long long divisors[11];
			for (int m = 0; m < 11; m++) divisors[m] = -1;

			for (int m = 2; m <= 10; m++) {
				long long bval = trans(val, m);
				long long divisor = find_divisor(bval);
				if (divisor == -1)
					break;
				values[m] = bval;
				divisors[m] = divisor;
			}

			bool flag = true;
			for (int m = 2; m <= 10; m++) {
				if (divisors[m] == -1)
					flag = false;
			}

			if (flag) {
				cnt++;
				printf("%lld", trans(val, 10));
				for (int m = 2; m <= 10; m++) {
					printf(" %d", divisors[m]);
				}
				printf("\n");

				if (cnt == J)
					break;
			}

		}


	}

	return 0;
}