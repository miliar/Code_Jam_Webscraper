/*
* Google Code Jam 2014
* Round 1B
* Adrian Dale
* B - New Lottery Game
*/
#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long ULL;

int T; // No of test cases

ULL SolveTestCase(ULL A, ULL B, ULL K)
{
	ULL caseCount = 0;
	for (ULL a = 0; a < A; ++a)
	{
		for (ULL b = 0; b < B; ++b)
		{
			if ((a&b) < K) ++caseCount;
		}
	}
	return caseCount;
}

void ReadTestCases()
{
	string line;

	getline(cin, line);
	istringstream parser(line);
	parser >> T;

	int TestNo = 1;
	while (TestNo <= T)
	{
		getline(cin, line);
		parser.str(line);
		parser.clear();
		ULL A, B, K;
		parser >> A >> B >> K;
		cout << "Case #" << TestNo << ": " << SolveTestCase(A, B, K) << endl;

		++TestNo;
	}
}

int main()
{
	ReadTestCases();
	//SolveTestCase(500, 4, 2000);
	return 0;
}
