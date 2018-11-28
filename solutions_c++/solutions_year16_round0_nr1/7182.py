#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t, count, start_number;
	int array[10];
	string string_number;
	bool done;

	cin >> t;

	for (int i = 1; i <= t; i++) {

		cin >> string_number;

		start_number = stoi(string_number);

		for (int j = 0; j < 10; j++) {
			array[j] = 0;
		}

		count = 0;

		done = false;

		while (done == false) {
			done = true;

			if (stoi(string_number) != 0)
			{
				for (int j = 0; j < string_number.length(); j++) {
					array[string_number[j] - '0']++;
				}

				for (int j = 0; j < 10; j++) {
					if (array[j] == 0)
						done = false;
				}

				if (done == false) {
					count++;
					string_number = to_string(start_number * (count + 1));
				}
			}
			else
				count = -1;
		}

		if (count == -1)
			cout << "Case #" << i << ": INSOMNIA\n";
		else
			cout << "Case #" << i << ": " << string_number << "\n";
	}

	return 0;
}