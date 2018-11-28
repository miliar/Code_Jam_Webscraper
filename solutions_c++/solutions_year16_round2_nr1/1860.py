#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <functional>

using namespace std;
typedef long long ll;

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());

	ofstream outputfile;
	outputfile.open("Output.txt");

	string line, S;
	
	int T = 0;


	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);


		for (int i = 0; i < T; ++i)
		{
			map<char, int> mapChar;
			int result[10];

			for (size_t i = 0; i < 10; i++)
			{
				result[i] = 0;
			}

			outputfile << "Case #" << i + 1 << ": ";

			getline(file, S);

			for (size_t k = 0; k < S.size(); k++)
			{
				mapChar[S[k]]++;
			}

			while (mapChar['Z']>0)
			{
				mapChar['Z']--;
				mapChar['E']--;
				mapChar['R']--;
				mapChar['O']--;
				result[0]++;
			}
			while (mapChar['W']>0)
			{
				mapChar['T']--;
				mapChar['W']--;
				mapChar['O']--;
				result[2]++;
			}
			while (mapChar['U']>0)
			{
				mapChar['F']--;
				mapChar['O']--;
				mapChar['U']--;
				mapChar['R']--;
				result[4]++;
			}
			while (mapChar['X']>0)
			{
				mapChar['S']--;
				mapChar['I']--;
				mapChar['X']--;
				result[6]++;
			}
			while (mapChar['G']>0)
			{
				mapChar['E']--;
				mapChar['I']--;
				mapChar['G']--;
				mapChar['H']--;
				mapChar['T']--;
				result[8]++;
			}
			while (mapChar['O']>0)
			{
				mapChar['O']--;
				mapChar['N']--;
				mapChar['E']--;
				result[1]++;
			}
			while (mapChar['F']>0)
			{
				mapChar['F']--;
				mapChar['I']--;
				mapChar['V']--;
				mapChar['E']--;
				result[5]++;
			}
			while (mapChar['V']>0)
			{
				mapChar['S']--;
				mapChar['E']--;
				mapChar['V']--;
				mapChar['E']--;
				mapChar['N']--;
				result[7]++;
			}
			while (mapChar['H']>0)
			{
				mapChar['T']--;
				mapChar['H']--;
				mapChar['R']--;
				mapChar['E']--;
				mapChar['E']--;
				result[3]++;
			}
			while (mapChar['N']>0)
			{
				mapChar['N']--;
				mapChar['I']--;
				mapChar['N']--;
				mapChar['E']--;
				result[9]++;
			}

			for (size_t i = 0; i < 10; i++)
			{
				while (result[i] > 0)
				{
					outputfile << i;
					result[i]--;
				}
			}

			outputfile << endl;
		}
	}

	file.close();

	outputfile.close();

	return 0;
}