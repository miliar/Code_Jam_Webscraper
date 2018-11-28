#include <iostream>
#include <fstream>
#include <unordered_map>
using namespace std;

int main()
{
	int numberOfTestCases = 0;
	string inputLine = "";
	char input;
	int i;
	int j = 0;
	unordered_map<int, int> hashtable;
	vector<unordered_map<int, int>> finalOutput;

	ifstream fin("in.txt");
	if (fin.is_open())
	{
		while (!fin.eof())
		{
			fin.get(input);

			if (input == '\n')
			{
				if (numberOfTestCases == 0)
				{
					numberOfTestCases = atoi(inputLine.c_str());
					inputLine = "";
					continue;
				}

				i = 0;
				for (char c : inputLine)
				{
					hashtable.emplace(i, c - '0');
					i++;
				}
				if (hashtable.size() != 0)
				{
					finalOutput.push_back(hashtable);
					hashtable.clear();
					inputLine = "";
				}
				continue;
			}

			if (input == ' ')
			{
				inputLine = "";
				continue;
			}
			inputLine = inputLine + input;
		}
	}
	fin.close();
	
	ofstream fout("out.txt");
	if (fout.is_open())
	{
		int totalStandups, requiredNumberOfFriends, newNumberOfFriends;
		char output[20];
		for (int i = 0; i < numberOfTestCases; i++)
		{
			totalStandups = 0;
			requiredNumberOfFriends = 0;
			newNumberOfFriends = 0;

			hashtable = finalOutput[i];
			for (int j = 0; j < hashtable.size(); j++)
			{
				if (totalStandups < j)
				{
					newNumberOfFriends = j - totalStandups;
					requiredNumberOfFriends += newNumberOfFriends;
				}
				else
				{
					newNumberOfFriends = 0;
				}
				totalStandups = totalStandups + newNumberOfFriends + hashtable[j];
			}
			sprintf_s(output, "Case #%d: %d\n", i + 1, requiredNumberOfFriends);
			fout << output;		
		}
	}
	fout.close();
	return 0;
}