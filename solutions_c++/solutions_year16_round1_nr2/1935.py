#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream inFile("input.txt");
	ofstream outFile("output.txt");
	int numCases, length; //length is the length of one side of the grid
	string word;

	if (!inFile)
	{
		cout << "File not working" << endl;
		return 0;
	}

	inFile >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		inFile >> length;

		outFile << "Case #" << i + 1 << ": ";

		vector<int> missing;
		vector<int> toCount;

		for (int j = 0; j < length*((length * 2) - 1); j++)
		{
			int next;
			inFile >> next;
			toCount.push_back(next);;
		}

		for (int j = 0; j < toCount.size(); j++)
		{
			size_t checkCount = count(toCount.begin(), toCount.end(), toCount[j]);
			if (checkCount % 2 != 0 && find(missing.begin(), missing.end(), toCount[j]) == missing.end())
			{
				missing.push_back(toCount[j]);
			}
		}

		sort(missing.begin(), missing.end());

		for (int j = 0; j < missing.size(); j++)
		{
			outFile << missing[j] << " ";
		}

		outFile << endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}