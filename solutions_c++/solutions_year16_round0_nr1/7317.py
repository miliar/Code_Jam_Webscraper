#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <tuple>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <cstdlib>
#include <stack>
#include <map>

using namespace std;

#define INF 1987654321
#define MAX 1000000
#define MOD 1000000007
#define CHK 1023

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int TC;
	long long int N, tmp;
	int i;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		bool digit[10] = { false, };
		scanf("%lld", &N);
		bool chk = false;
		for (i = 1; i < MAX; i++) {
			tmp = N * i;
			while (tmp) {
				digit[tmp % 10] = true;
				bool c = false;
				for (int a = 0; a < 10; a++) {
					if (!digit[a]) {
						c = true;
						break;
					}
				}
				// ¿Ï·á
				if (!c) {
					chk = true;
					break;
				}
				tmp /= 10;
			}
			if (chk) break;
		}

		printf("Case #%d: ", tc);

		if (chk)
			printf("%lld\n", N * i);
		else
			printf("INSOMNIA\n");
	}

	return 0;
}