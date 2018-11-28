#include <bits/stdc++.h>

int main() {
	short k;
	short c;
	
	scanf("%hi", &k);
	c = k;
	
	while (k--) {
		int n;
		int x;
		int y;
		bool d[10] = {false};
		int i = 1;

		scanf("%d", &n);

		if (n == 0) {
			printf("Case #%hi: INSOMNIA\n", c-k);
			continue;
		}
		
		while (!(d[0] && d[1] && d[2] && d[3] && d[4] && d[5] && d[6]
				&& d[7] && d[8] && d[9])) {
			x = y = n * i++;

			while (x) {
				d[x % 10] = true;
				x /= 10;
			}
		}


		printf("Case #%hi: %d\n", c-k, y);
	}
	
	return 0;
}
