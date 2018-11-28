#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

void seperateDig(int input, int DigitCount[])
{
	while (input != 0)
	{
		int rem = input % 10;
		DigitCount[rem] = rem;
		input = input / 10;
	}
}

bool check(int DigitCount[])
{
	bool fillAll = true;
	for (size_t j = 0; j < 10; j++)
	{
		if (DigitCount[j] != j)
		{
			fillAll = false;
			break;
		}
	}

	return fillAll;
}

int main()
{
	int T;
	cin >> T;

	int CASE = 1;
	int DigitCount[10];

	while (T--)
	{
		for (size_t i = 0; i < 10; i++)
			DigitCount[i] = -1;

		int input;
		cin >> input;
		
		if (input == 0)
		{
			cout << "Case #" << CASE << ": " << "INSOMNIA" << endl;
		}
		else
		{
			int k = 1;
			while (check(DigitCount) != true)
			{
				seperateDig(input * k, DigitCount);
				k++;
			}

			cout << "Case #" << CASE << ": " << input * (k - 1)<< endl;
		}


		CASE++;
		//cin.ignore();
	}

	cin.get();
	return 0;
}