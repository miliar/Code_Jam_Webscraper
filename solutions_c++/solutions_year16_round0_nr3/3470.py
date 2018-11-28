#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <math.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int t, n, jams;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n >> jams;  // read n and then m.
		vector<vector<long long int>> divisors;
		vector<long long int> plain_jams;
		for (int k = 0; k < pow(2, n - 2); ++k)
		{
			vector<int> current_jam;
			long long int current_jam_plain = 0;
			current_jam.push_back(1);
			current_jam_plain += pow(10, n - 1);
			long long int temp = k;
			for (int j = 0; j < n - 2; ++j)
			{
				current_jam_plain += (temp % 2) * pow(10, n - 2 - j);
				current_jam.push_back(temp % 2);
				temp = temp / 2;
			}
			current_jam.push_back(1);
			current_jam_plain++;
			bool skip_jam = false;
			vector<long long int> divisor;
			for (int base = 2; base <= 10; ++base)
			{
				long long int number = 0;
				for (int digit = n-1; digit >= 0; --digit)
				{
					number += current_jam[digit] * pow(base, n-digit-1);
				}

				bool found_divisor = false;
				for (long long int divide = 2; divide < number / divide; ++divide)
				{
					if (floor(double(number) / (double)divide) * divide == number)
					{
						divisor.push_back(divide);
						found_divisor = true;
						break;
					}
				}
				if (!found_divisor)
				{
					skip_jam = true;
					break;
				}
			}
			if (skip_jam == true)
			{
				continue;
			}
			else
			{
				divisors.push_back(divisor);
				plain_jams.push_back(current_jam_plain);

				if (divisors.size() == jams)
				{
					break;
				}
			}
		}

		cout << "Case #" << i << ":" << endl;
		for (int j = 0; j < divisors.size(); ++j)
		{
			cout << plain_jams[j] << " ";
			for (int k = 0; k < 9; ++k)
			{
				cout << divisors[j][k] << " ";
			}
			cout << endl;
		}
	}
}