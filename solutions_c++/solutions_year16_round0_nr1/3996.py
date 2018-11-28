#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	long long int t, n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		int counts[10] = { 0 };
		int total_count = 0;
		long long int temp = n;
		while (temp > 0)
		{
			int digit = temp % 10;
			if (counts[digit] == 0)
			{
				counts[digit] = 1;
				total_count++;
			}
			temp = temp / 10;
		}

		if (total_count == 0)
		{
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}

		long long int multiplier = 2;
		
		while (true)
		{
			temp = multiplier * n;
			while (temp > 0)
			{
				int digit = temp % 10;
				if (counts[digit] == 0)
				{
					counts[digit] = 1;
					total_count++;
				}
				temp = temp / 10;
			}

			if (total_count == 10)
			{
				break;
			}
			else
			{
				multiplier++;
			}

		}
		cout << "Case #" << i << ": " << multiplier * n << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}