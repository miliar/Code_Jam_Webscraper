#include <iostream>
#include <stdio.h>

using namespace std;

uint16_t digitsIn(unsigned long long int X) {
	uint16_t seenDigits = 0;
	for (int i = 0; i < 10 && X > 0; i++)
	{
		seenDigits |= (1 << (X % 10));
		X /= 10;
	}
	return seenDigits;
}

int main()
{
	unsigned int T;

	scanf("%u", &T);

	for (unsigned int i = 1; i <= T; i++) 
	{
		unsigned long long int N;
		scanf("%llu", &N);

		if (N == 0)
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}

		uint16_t seenDigits = 0;
		unsigned long long int X = 0;
		while (seenDigits < 0x3FF)
		{
			X += N;
			seenDigits |= digitsIn(X);
		}
		cout << "Case #" << i << ": " << X << endl;
	}
}
