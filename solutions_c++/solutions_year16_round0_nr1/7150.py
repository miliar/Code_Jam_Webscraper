#include <iostream>
#include <cmath>
#include <unistd.h>

#define debug(i) cout << "Error" << i << '\n';

using namespace std;

int main(int argc, char const *argv[])
{
	int T(0);

	cin >> T;

	for (int p = 1; p <= T; ++p)
	{
		bool digits_seen[10] = {false};
		long int N(0);
		int no_of_zeroes(0);

		// Code to take input
		cin >> N;

		// // Code to remove any trailing zeroes
		// int last_digit(N%10);
		// while (last_digit == 0 and N != 0)
		// {
		// 	N = N/10;
		// 	last_digit = N%10;
		// 	++no_of_zeroes;
		// }

		// Conditions for zero
		if ( N == 0)
		{
			cout << "Case #" << p << ": " << "INSOMNIA" << '\n';
			continue;
		}

		long int i(N);
		for (;; i += N)
		{
			// Code to find the digits in number i
			long int temp_i = i;
			while (temp_i != 0)
			{
				digits_seen[temp_i%10] = true;
				temp_i = temp_i/10;
			}

			// Check function to ensure that all the digits are seen
			bool check = true;
			for (int j = 0; j < 10; ++j)
			{
				check = check and digits_seen[j];
			}

			if (check == true)
				break;
		}

		cout << "Case #" << p << ": " << i*(long int)pow(10, no_of_zeroes) << '\n';
	}

	return 0;
}