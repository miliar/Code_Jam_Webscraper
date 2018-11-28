#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
int main() {
	int n, x, i, j, v, r, s;
	cin >> n;
	bool y[11];
	for (j = 1; j <=n; j++) {
		printf("Case #%d: ", j);
		cin >> x;
		if (!x) {
			puts("INSOMNIA");
			continue;
		}
		memset(y, 0, sizeof(y));
		s = 0;
		i = 1;
		while (1) {
			v = i * x;
			while (v) {
				r = v % 10;
				if (!y[r]) {
					y[r] = 1;
					s++;
				}
				v /= 10;
			}
			if (s == 10) {
				printf("%d\n", i * x);
				break;
			}
			i++;
		}
	}
	return 0;
}
