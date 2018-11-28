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
	string line;
	int T = 0;
	ll result;

	vector<ll> numberofFlips;
	char prevChar;

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		numberofFlips.resize(T);

		for (int i = 0; i < T; ++i)
		{
			getline(file, line);
			istringstream ss(line);
			
			result = 0;
			prevChar = line[0];

			for (int i = 1; i < line.size(); i++)
			{
				if (line[i] != prevChar)
				{
					result++;
				}

				prevChar = line[i];
			}

			if (prevChar == '-')
			{
				result++;
			}
			
			numberofFlips[i] = result;
		}
	}
	
	file.close();

	ofstream outputfile;
	outputfile.open("Output.txt");

	for (int i = 0; i < T - 1; ++i)
	{
		outputfile << "Case #" << i + 1 << ": " << numberofFlips[i] << endl;
	}
	outputfile << "Case #" << T << ": " << numberofFlips[T - 1];
	
	outputfile.close();

	return 0;
}