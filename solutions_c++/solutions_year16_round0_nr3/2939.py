#include <cstdio>
#include <cstdlib>
#include <cstring>

typedef __uint128_t integer;

integer primes[20] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73};

void print_integer(integer bin) {
	char buff[42] = "";
	buff[41] = '\0';
	int i = 40;
	while (bin) {
		buff[i--] = (bin % 10) + '0';
		bin /= 10;
	}
	printf("%s", buff+i+1);
	// for (int i = 0; i < sizeof(integer); ++i) {
	// 	unsigned char c = bin % 0xff;
	// 	bin >>= 8;
	// 	putchar(c);
	// }
}

int divisor(integer number) {
	for (int i = 0; i < 20; ++i)
		if (number % primes[i] == 0) {
			return primes[i];
		}
	return 0;
}

integer to_system(integer bin, int system) {
	integer result = 0, radix = 1;
	while (bin) {
		if (bin % 2 == 1)
			result += radix;
		bin >>= 1;
		radix *= system;
	}
	return result;
}

int main(int argc, char const *argv[]) {

	integer numbers[9];
	integer adds[9];
	integer buffer[9];

	for (int i = 0; i < 9; ++i)
		// adds[i] = (i+1)*(i+2);
		adds[i] = (i+2);


	int T, J, N;
	scanf("%d\n", &T);

	for (int i = 0; i < T; ++i) {
		scanf("%d %d", &N, &J);
		printf("Case #%d:\n", i+1);

		integer bin = 1;
		bin = (bin << (N-1)) + 1;

		for (int i = 0; i < 9; ++i) 
			numbers[i] = to_system(bin, i + 2);

		int idx = 0;
		while(J) {
			++idx;
			int i;
			for (i = 0; i < 9; ++i) {	
				int number = numbers[i];
				int div = divisor(numbers[i]);
				buffer[i] = divisor(numbers[i]);
				if (!buffer[i])
					break;
			}
			if (i == 9) {
				print_integer(numbers[8]);
				for (int i = 0; i < 9; ++i)
					printf(" %ld", buffer[i]);
				--J;
				printf("\n");
			}

			numbers[0] += adds[0];
			for (i = 1; i < 9; ++i) 
				numbers[i] = to_system(numbers[0], i + 2);
		}


	}

	return 0;
}