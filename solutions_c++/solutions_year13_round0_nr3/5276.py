#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>

bool palindrome(int number) {
	int q, r, reverse = 0, n;
	n = number;
	while (n != 0) {
		q = n / 10;
		r = n % 10;
		n = q;
		reverse *= 10;
		reverse += r;
	}
	return (number == reverse);
}

int rootSquare(int number) {
	int result = (int) pow((double) number, (1.0 / 2.0));
	return ((result * result) == number) ? result : -1;
}

int main() {

	int cases, a, b;
	int aux, total;
	while (scanf("%d", &cases) == 1) {
		for (int c = 1; c <= cases; c++) {
			scanf("%d %d", &a, &b);
			total = 0;
			for (int i = a; i <= b; i++) {
				if (palindrome(i)) {
					aux = rootSquare(i);
					if (aux == -1) {
						//
					} else {
						if (palindrome(aux))
							total++;
					}
				}
			}
			printf("Case #%d: %d\n", c, total);
		}
	}

	return 0;
}