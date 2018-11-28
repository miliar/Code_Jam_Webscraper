#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

typedef long long LL;

int main() {
	int T;
	scanf("%d", &T);
	for (int TI = 1; TI <= T; ++TI) {
		int n;
		scanf("%d", &n);
		bool num[13] = {0};
		printf("Case #%d: ", TI);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		for (int i = n, k = 10; k; i += n) {
			for (int j = i; j > 0; j /= 10)
				if (!num[j % 10]) {
					num[j % 10] = 1;
					--k;
				}
			if (k == 0) printf("%d\n", i);
		}
	}
	return 0;
}
