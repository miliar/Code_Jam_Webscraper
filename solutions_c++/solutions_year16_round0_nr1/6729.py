#include <iostream>
#include <stdint.h>

using namespace std;

void main()
{
	unsigned int testCases;
	cin >> testCases;
	for (unsigned int t = 1; t <= testCases; t++)
	{
		uint32_t n;
		cin >> n;

		uint16_t result = 0;
		result = result | 63;

		if (n == 0)
		{
			cout << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}
		uint64_t i = 1;
		uint64_t number;
		uint64_t temp;
		uint16_t mask = 32768;
		for (;;)
		{
			number = n * i++;
			temp = number;
			while (temp != 0)
			{
				uint8_t rem = temp % 10;
				result = result | (mask >> rem);
				temp = temp / 10;
			}
			if (result == 65535)
			{
				break;
			}
		}
		cout << "Case #" << t << ": " << number << endl;
	}
}