#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define SMAX 1005

int main() {
	int t;
	scanf("%d", &t);
	char str[SMAX];

	for (int ctest = 1; ctest <= t; ctest++) {
		int smax;
		scanf("%d", &smax);

		scanf(" %s", str);

		ll current = 0;
		ll toadd = 0;
		int len = strlen(str);
		for (int i = 0; i < len; i++) {
			int d = str[i] - '0';
			if (d > 0 && i > current) {
				ll dx = i - current;
				toadd += dx;
				current += dx;
			}

			current += d;
		}

		printf("Case #%d: %lld\n", ctest, toadd);
	}
	
	return 0;
}
