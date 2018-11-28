#include <bits/stdc++.h>

int main() {
	int t, n, curr, j, i, k;
	long long int no;
	int marked[10];
	bool flag;

	scanf("%d", &t);

	for (k = 1; k <= t; k++) {
		std::fill(marked, marked + 10, 0);
		scanf("%d", &n);

		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", k);
		} else {
			j = 1;
			flag = true;
			no = n;
			while (flag) {
				while (no) {
					curr = no % 10;
					no = no / 10;
					if (!marked[curr]) {
						marked[curr] = 1;
					}
				}
				flag = false;
				for (i = 0; i < 10; i++) {
					if (marked[i] == 0) {
						flag = true;
						break;
					}
				}
				j++;
				no = n * j;
			}
			no = n * (j - 1);
			printf ("Case #%d: %lld\n", k, no);
		}
	}
	return 0;
}
			
			