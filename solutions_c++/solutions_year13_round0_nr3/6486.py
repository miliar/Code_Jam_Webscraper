#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int MAX_SIZE = 1100;

bool is_palindrome(string number)
{
	int i = 0, j = number.size() - 1;

	while (j - i > 1)
	{
		if (number[i] != number[j])
			break;

		i++;
		j--;
	}

	if ((j == i or j - i == 1) and number[i] == number[j])
		return true;

	return false;
}

int main()
{
	int no_tests;

	cin >> no_tests;

	for (int current_test = 0; current_test < no_tests; current_test++)
	{
		int A, B, counter = 0;

		cin >> A >> B;

		int current = sqrt(A);

		if (current * current < A)
			current++;

		char converter[MAX_SIZE];

		// We only need to check the real squares.
		while(current*current <= B)
		{
			sprintf(converter,"%d",current);

			if (is_palindrome(string(converter)))
			{
				sprintf(converter,"%d",current*current);

				if (is_palindrome(string(converter)))
					counter++;
			}

			current++;
		}

		cout << "Case #" << (current_test + 1) << ": " << counter;

		if (current_test < no_tests - 1)
			cout << endl;

	}
}