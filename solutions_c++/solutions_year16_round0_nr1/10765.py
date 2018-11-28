#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

void sayDigits(vector<bool>& digitsSayed, int& numberOfDigitsSayed, int number)
{
	if (number == 0)
	{
		if (!digitsSayed[0])
		{
			numberOfDigitsSayed++;
			digitsSayed[0] = true;
		}
	}
	else 
	{
		while (number > 0)
		{
			int lastDigit = number % 10;
			if (!digitsSayed[lastDigit])
			{
				numberOfDigitsSayed++;
				digitsSayed[lastDigit] = true;
			}
			number /= 10;
		}
	}
}

int main() 
{
	int T, N;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cin >> N;
		int currentNumber = 0;
		int numberOfDigitsSayed = 0;
		vector<bool> digitsSayed(10, false);
		if (N != 0)
		{
			while (numberOfDigitsSayed < 10 && UINT_MAX - N > currentNumber)
			{
				currentNumber += N;
				sayDigits(digitsSayed, numberOfDigitsSayed, currentNumber);
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (numberOfDigitsSayed < 10)
			cout << "INSOMNIA" << endl;
		else
			cout << currentNumber << endl;
	}
	return 0;
}