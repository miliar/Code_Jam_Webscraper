#include <algorithm>
#include <cstring>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

bool isPalindrome(int number)
{
	int rem;
	int sum = 0;
	int copy;

	copy = number;

	while(copy != 0)
	{
		rem = copy % 10;
		copy = copy / 10;
		sum = (sum * 10) + rem;

	}

	return number == sum;
}

bool isFairandSquare(int number)
{
	if (!isPalindrome(number))
		return false;

	int value = sqrt(number);

	if (number != value * value)
		return false;

	if (!isPalindrome(value))
		return false;

	return true;
}

int main ()
{
	int T = 0;
	int begin;
	int end;
	int count = 0;

	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		cin >> begin;
		cin >> end;
		count = 0;

		for (int number = begin; number <= end; number++)
		{
			count += isFairandSquare(number) ? 1 : 0;
		}
		cout << count << "\n";
	}
}
