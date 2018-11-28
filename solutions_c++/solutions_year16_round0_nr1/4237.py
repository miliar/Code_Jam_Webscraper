#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

#define NBIT_ON(D,N) ((D) |= (0x1 << N))
#define NBIT_FULL 0b1111111111
#define PMAX 10000

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; c++) {
		int digit;
		cin >> digit;

		if (digit == 0) {
			printf("Case #%d: INSOMNIA\n", c);			
		}
		else {
						
			int is_insomnia = 1;
			int bit_checker = 0;			
			int tmp, shifter, pdigit;
			for (int p = 1; p < PMAX; p++) {
				pdigit = tmp = digit * p;
				while (tmp) {
					shifter = tmp % 10;
					NBIT_ON(bit_checker, shifter);
					tmp /= 10;
				}

				if (bit_checker == NBIT_FULL) {
					printf("Case #%d: %d\n", c, pdigit);		
					is_insomnia = 0;
					break;
				}
			}

			if (is_insomnia) {
				printf("Case #%d: INSOMNIA\n", c);
			}

		}
	}

	return 0;
}