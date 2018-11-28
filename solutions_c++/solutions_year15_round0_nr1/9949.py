#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream inF;
	ofstream outF;

	inF.open("input.txt");
	outF.open("output.txt");

	int T;
	inF >> T;

	int *array;
	int max, totalF = 0;
	int sum = 0;
	char hold;

	for(int test = 1; test < T + 1; test++)
	{
		inF >> max;
		inF.ignore(100, ' ');
		max++;

		array = new int[max];

		for(int i = 0;i <= (max - 1);i++)
		{
			inF.get(hold);
			array[i] = static_cast<int>(hold) - 48;
		}

		for(int i = 0;i <= (max - 1);i++)
		{
			if (sum < i && array[i] != 0)
			{
				totalF += i - sum;
				sum += totalF;
			}

			sum += array[i];
		}

		outF << "Case #" << test << ": " << totalF << endl;

		sum = 0;
		totalF = 0;
		max = 0;
		delete []array;
	}

	return 0;
}
