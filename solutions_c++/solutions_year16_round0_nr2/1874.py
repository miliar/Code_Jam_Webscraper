#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
#include <sstream>
#include <istream>
#include <unordered_map>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int i = 0; i<numCases; i++)
	{
		string line;
		cin >> line;

		int minTimes = INT_MAX;
		int totalChange = 0;
		for (int i = 1; i<line.size(); i++)
		{
			if (line[i] != line[i - 1]) totalChange++;
		}
		if (line[line.size() - 1] == '+') minTimes = totalChange;
		else minTimes = totalChange + 1;

		cout << "Case #" << i + 1 << ": " << minTimes << endl;
	}

	return 0;
}