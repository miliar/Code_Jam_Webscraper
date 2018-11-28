//
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream inFile("input.txt");
	ofstream outFile("output.txt");
	int numCases, countBy, multiple, seenNum;
	bool hasAllNums;

	if (!inFile)
	{
		cout << "File not working" << endl;
		return 0;
	}
	
	inFile >> numCases;
	
	for (int i = 0; i < numCases; i++)
	{
		inFile >> countBy;

		hasAllNums = false;
		vector <int> nums = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

		outFile << "Case #" << i + 1 << ": ";

		if (countBy == 0)
		{
			 outFile << "INSOMNIA" << endl;
		}
		else
		{
			int j = 1;
			while (!hasAllNums)
			{
				multiple = j*countBy;
				int breakdown = multiple;

				while (breakdown > 0)
				{
					seenNum = breakdown % 10;
					nums.erase(std::remove(nums.begin(), nums.end(), seenNum), nums.end());

					breakdown = breakdown/10;

					if (nums.empty())
					{
						hasAllNums = true;
						break;
					}
				}
				j++;
			}
			outFile << multiple << endl;
		}
	}
	
	return 0;
}