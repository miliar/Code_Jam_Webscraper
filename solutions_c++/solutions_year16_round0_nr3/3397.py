#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <stack>
#include <queue>
#include <functional>
#include <algorithm>
using namespace std;

int T, N, J;

long long convert(int num, int base) {
	if (base == 2) return num;

	long long cur = 1, ret = 0;
	while (num) {
		ret += cur * (num & 1);
		cur *= base;
		num >>= 1;
	}
	return ret;
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		scanf("%d%d", &N, &J);
		printf("Case #%d:\n", test);

		for (int i = 0; i < (1 << (N - 2)); i++) {
			int cur = (1 << (N - 1)) | (i << 1) | 1;

			bool flag = true;
			vector<long long> result;
			for (int k = 2; k <= 10; k++) {
				long long num = convert(cur, k);

				flag = false;
				for (long long p = 2; p * p <= num; p++) {
					if (num % p == 0) {
						result.push_back(p);
						flag = true;
						break;
					}
				}

				if (!flag) break;
			}
			if (flag) {
				J--;
				printf("%lld", convert(cur, 10));
				for (auto num : result) {
					printf(" %lld", num);
				}
				puts("");

				if (J == 0) break;
			}
		}
	}

	return 0;
}
