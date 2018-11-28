#include <fstream>
#include <vector>
#include <iostream>
#include <limits>
#include <string>
#include <numeric>

bool digits[10] = { false };
int verify = 0;
int crntDigit = 0;

bool Check(int current) {
	if (!digits[current]) {
		digits[current] = true;
		verify++;
	}

	if (verify == 10) {
		return true;
	}
	return false;
}

void GetDigits(unsigned long num) {
	if (num > 9) {
		GetDigits(num / 10);
	}

	crntDigit = num % 10;
	num = num % 10;

	Check(crntDigit);
}

int main(){

	freopen("A-large.in", "r", stdin);
	freopen("Alarge.out", "w", stdout);
	
	unsigned int T;
	std::cin >> T;

	for (int i = 0; i < T; i++){
		printf("Case #%d: ", i + 1);

		long long N;
		std::cin >> N;

		if (N == 0) {
			std::cout << "INSOMNIA";
			printf("\n");
			memset(&digits, 0, sizeof(digits));
			verify = 0;
			crntDigit = 0;
			continue;
		}

		long long count = 1;
		while (verify < 10) {
			GetDigits((count*N));
			count++;
		}
		std::cout << ((count-1)*N);
		memset(&digits, 0, sizeof(digits));
		crntDigit = 0;
		verify = 0;

		printf("\n");
	}

}
