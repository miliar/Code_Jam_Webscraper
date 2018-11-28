//Ryan Lijewski 2016
//Google Code Jam - Counting Sheep

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool searchVector(vector<int> list, int number);

int main()
{
	ifstream inputFile;
	ofstream outputFile;
	int t;
	int n;
	int lastDigit;
	vector<int> tenDigits;
	int digit;
	int tempNumber;

	inputFile.open("C:\\Users\\Pxihcky35\\Documents\\Google_Code_Jam\\A-large.in");
	outputFile.open("C:\\Users\\Pxihcky35\\Documents\\Google_Code_Jam\\output-large.txt");

	if (inputFile)
	{
		//store number of test cases in t
		inputFile >> t;

		//loop through test cases
		for (int i = 1; i <= t; i++)
		{
			//starting number
			inputFile >> n;

			if (n == 0)
			{
				//output to file
				outputFile << "Case #" << i << ": " << "INSOMNIA" << endl;
			}
			else
			{
				//factor to multiply by
				int j = 1;

				while (tenDigits.size() < 10)
				{
					tempNumber = n * j;
			
					//divisor to parse int
					int divisor = 10;

					lastDigit = tempNumber % 10;

					if (!searchVector(tenDigits, lastDigit))
					{
						tenDigits.push_back(lastDigit);
					}

					while (tempNumber / divisor != 0)
					{
						digit = (tempNumber / divisor) % 10;

						if (!searchVector(tenDigits, digit))
						{
							tenDigits.push_back(digit);
						}

						divisor *= 10;
					}

					j++;
				}

				//output to file
				outputFile << "Case #" << i << ": " << tempNumber << endl;

			}

			tenDigits.clear();
		}

	}
	else
	{
		cout << "Error opening file." << endl;
	}

	inputFile.close();
	outputFile.close();

    return 0;
}

bool searchVector(vector<int> list, int number)
{
	int index = 0;
	bool found = false;
	while (index < list.size() && !found)
	{
		if (list[index] == number)
		{
			found = true;
		}
		index++;
	}

	return found;
}