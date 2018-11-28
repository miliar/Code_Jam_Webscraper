#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t, count, pos, startsign;
	string pancakes;
	bool done;

	cin >> t;

	for (int i = 1; i <= t; i++) {

		cin >> pancakes;

		done = false;
		count = 0;

		while (done == false) {
			done = true;
			for (int j = 0; j < pancakes.length(); j++) {
				if (pancakes[j] == '-')
					done = false;
			}

			pos = 0;
			startsign = pancakes[0];

			while (startsign == pancakes[pos]) {
				pos++;
			}

			for (int j = 0; j < pos; j++) {
				if (startsign == '+')
					pancakes[j] = '-';
				else
					pancakes[j] = '+';
			}

			if (done != true)
				count++;
		}


		cout << "Case #" << i << ": " << count << "\n";
	}

	return 0;
}