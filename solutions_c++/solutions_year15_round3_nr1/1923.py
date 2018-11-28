#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <bitset>
#include <sstream>

/*
Inputs:
-Number of test cases
-The number of rows on the board
-The number of columns on the board
-The width of the ship

Outputs:
"Case #x: y"
where x is the test case and y "NOT POSSIBLE" if not a valid combination, or the minimum score you can achieve.
*/

#define ul unsigned long long
#define ui unsigned int
#define sl signed long long
#define si signed int

using namespace std;

string solve(ul r, ul c, ul w)
{
	ul s = 0;

	s += (c / w) * r;
	s += (w - 1);

	if (c % w != 0)
	{
		s += 1;
	}

	if (w == c)
	{
		s = w;
	}

	return to_string(s);
}

int main(int argc, char* argv[])
{
	unsigned int testCases = 0;
	cin >> testCases;

	vector<string> testCaseYs;

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		string testCaseY;
		ul r, c, w;

		cin >> r >> c >> w;

		testCaseYs.push_back(solve(r, c, w));
	}

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		cout << "Case #" << tc + 1 << ": " << testCaseYs[tc] << endl;
	}
}
