//
//  CountingSheep.cpp
//
//
//  Created by Laszlo Majer on 09/04/16.
//
//


#include <iostream>
#include <string>


using namespace std;


int main()
{
	int T = 0;
	
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		uint64_t N;
		cin >> N;
		
		cout << "Case #" << i + 1 << ": ";
		if (N == 0)
			cout << "INSOMNIA" << endl;
		else
		{
			uint64_t last = N;
			bool digits[10];
			memset(digits, false, 10);
			bool expected[10];
			memset(expected, true, 10);

			while (true)
			{
				// Add seen digits
				uint64_t tmp = last;
				while (tmp)
				{
					digits[tmp % 10] = true;
					tmp /= 10;
				}

				if (memcmp(digits, expected, 10) == 0)
					break;
				
				last += N;
			}
			cout << last << endl;
		}
	}
}
