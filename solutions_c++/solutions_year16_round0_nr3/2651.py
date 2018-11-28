#include <iostream>
#include <cstdio>
#include <cstring>  
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

long long ans[20];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n, m;
		scanf("%d%d", &n, &m);
		printf("Case #%d:\n", o + 1);
		int cnt = 0;
		for (int i = (1 << (n - 1)) + 1; i < (1 << n); i += 2) {
			bool flag = 1;
			long long k;
			for (int p = 2; p < 11; ++p) {
				long long x = i, y = 0, z = 1;
				while (x) {
					y += z * (x % 2);
					z *= p;
					x /= 2;
				}
				k = y;
				flag = 0;
				for (int j = 2; j < sqrt(y) + 1; ++j) {
					if (y % j == 0) {
						ans[p] = j;
						flag = 1;
						break;
					}
				}
				if (!flag) break;
			}
			if (flag) {
				++cnt;
				printf("%lld", k);
				for (int i = 2; i < 11; ++i) {
					printf(" %lld", ans[i]);
				}
				printf("\n");
				if (cnt == m) break;
			}
		}
	}
	return 0;
}


