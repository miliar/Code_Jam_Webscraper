#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>

using namespace std;

typedef unsigned long long ULL;

int main(int argc, char** argv) {
	int T;
	int test_case;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case) {
		int N, J;
		scanf("%d %d", &N, &J);


		printf("Case #%d:\n", test_case);
		ULL nonTri[11] = { 0, };
		ULL start = pow(2, N - 2);
		ULL end = start << 1;
		int cnt = 0;
		for (; start < end; start++) {
			bool found = true;
			for (ULL i = 2; i <= 10; i++) {
				ULL n = (start << 1) + 1;
				if (i > 2) {
					ULL nn = 0;
					ULL add = 1;
					while (n > 0) {
						if (n & 1)
							nn += add;
						add *= i;
						n >>= 1;
					}
					n = nn;
				}
				
				if (n & 1) {
					bool prime = true;
					for (ULL j = 3ll; j * j <= n; j += 2) {
						if (n % j == 0) {
							nonTri[i] = j;
							prime = false;
							break;
						}
					}
					if (prime)
						found = false;
				}
				else {
					nonTri[i] = 2;
				}
			}

			if (found) {
				cnt++;

				char str[32] = { 0, };
				ULL n = (start << 1) + 1;
				for (int i = 0; n > 0; i++) {
					str[i] = n & 1;
					n >>= 1;
				}
				
				for (int i = N - 1; i >= 0; i--)
					printf("%d", str[i]);
				printf(" ");

				for (int i = 2; i <= 10; i++) {
					printf("%d ", nonTri[i]);
				}
				printf("\n");
			}

			if (cnt >= J)
				break;
		}
	}

	return 0;
}