#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

bool mark[10];
int digitsLeft;

int T;
long long n;

void markDigits(long long number)
{
	while (number > 0) {
		int lastDigit = number % 10;
		if (!mark[lastDigit]) {
			digitsLeft--;
			mark[lastDigit] = true;
		}

		number /= 10LL;
	}
}

int main()
{
	scanf("%d",&T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ",t);

		scanf("%lld",&n);

		if (n == 0LL) {
			printf("INSOMNIA\n");
			continue;
		}

		memset(mark, 0, sizeof(mark));
		digitsLeft = 10;

		long long currentNumber = n;
		markDigits(currentNumber);
		while (digitsLeft > 0) {
			currentNumber += n;
			markDigits(currentNumber);
		}

		printf("%lld\n",currentNumber);
	}

	return 0;
}