#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream inFile("input.txt");
	ofstream outFile("output.txt");
	int numCases;
	string word;

	if (!inFile)
	{
		cout << "File not working" << endl;
		return 0;
	}

	inFile >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		outFile << "Case #" << i + 1 << ": ";

		inFile >> word;
		string lastWord = "";

		lastWord = word[0];

		for (int j = 1; j < word.length(); j++)
		{
			if (word[j] < lastWord[0])
			{
				lastWord = lastWord + word[j];
			}
			else
			{
				lastWord = word[j] + lastWord;
			}
		}

		outFile << lastWord << endl;
	}


	return 0;
}