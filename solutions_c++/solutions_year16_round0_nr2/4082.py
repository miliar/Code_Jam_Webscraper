#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	long long int t, n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		char input[1500];
		cin >> input;  // read n and then m.
		long long int count = 0;
		long long int flips = 0;
		while (input[count] != '\0')
		{
			if (input[count] != input[count + 1] && input[count + 1] != '\0')
			{
				if (input[count] == '+')
				{
					flips += 2;
					int k = 1;
					while (true)
					{
						if (input[count + k] == '-')
						{
							input[count + k] = '+';
							k++;
						}
						else
						{
							break;
						}
					}
				}
				else
				{
					flips += 1;
				}
			}
			count++;
		}

		if (flips == 0)
		{
			if (input[0] == '-')
			{
				flips = 1;
			}
		}
		
		cout << "Case #" << i << ": " << flips << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}