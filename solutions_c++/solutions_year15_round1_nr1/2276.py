#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <bitset>
#include <sstream>

/*
Inputs:
-Number of test cases
-Number of 10 second intervals mushrooms

Outputs:
"Case #x: y z"
where x is the test case and y is using first method, and z is using second method.
*/

using namespace std;

string solveA(vector<unsigned long> shrooms)
{
	unsigned long count = 0;
	for (unsigned long i = 0; i < shrooms.size() - 1; i += 1)
	{
		if (shrooms[i] > shrooms[i + 1])
		{
			count += shrooms[i] - shrooms[i + 1];
		}
	}
	return to_string(count);
}
string solveB(vector<unsigned long> shrooms)
{
	unsigned long rate = 0;
	for (unsigned long i = 0; i < shrooms.size() - 1; i += 1)
	{
		if (shrooms[i] > shrooms[i + 1])
		{
			rate = max(rate, shrooms[i] - shrooms[i + 1]);
		}
	}

	unsigned long count = 0;
	for (unsigned long i = 0; i < shrooms.size() - 1; i += 1)
	{
		count += min(rate, shrooms[i]);
	}
	return to_string(count);
}

int main(int argc, char* argv[])
{
	unsigned int testCases = 0;
	cin >> testCases;

	vector<string> testCaseYs;
	vector<string> testCaseZs;

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		string testCaseY;
		unsigned long count;
		vector<unsigned long> mushrooms;

		cin >> count;
		for (unsigned long i = 0; i < count; i += 1)
		{
			unsigned long temp;
			cin >> temp;
			mushrooms.push_back(temp);
		}

		testCaseYs.push_back(solveA(mushrooms));
		testCaseZs.push_back(solveB(mushrooms));
	}

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		cout << "Case #" << tc + 1 << ": " << testCaseYs[tc] << " " << testCaseZs[tc] << endl;
	}
}
