#include <iostream>
#include <stdint.h>
using namespace std;

int main()
{
	uint32_t T = 0; 
	uint32_t Smax = 0;
	uint8_t counts[1002] = {0};

	cin >> T;
	for (uint32_t case_num = 1; case_num <= T; case_num++)
	{
		cin >> Smax >> counts;
		uint32_t sum = counts[0] - 48;
		uint32_t friends = 0;

		for (uint32_t i = 1; i <= Smax; i++)
		{
			if (sum < i)
			{
				friends += (i - sum);
				sum += (i - sum);
			}

			sum += (counts[i] - 48);
		}

		cout << "Case #" << case_num << ": " << friends << endl;
	}

	return 0;
}