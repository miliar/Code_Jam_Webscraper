#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream inFile;
ofstream outFile;

long long minDiff = numeric_limits<long long>::max();
string resultC, resultJ;

long long rC, rJ;

void dfs(int pos, string& C, string& J)
{
	//cout << C << " " << J << endl;
	if (pos <= C.size())
	{
		int Index = C.size() - pos;
		if (C[Index] == '?' && J[Index] == '?')
		{
			
			for (int i = 0; i <= 9; ++i)
			{
				for (int j = 0; j <= 9; ++j)
				{
					char c1 = C[Index];
					char c2 = J[Index];

					C[Index] = '0' + i;
					J[Index] = '0' + j;
					dfs(pos + 1, C, J);

					C[Index] = c1;
					J[Index] = c2;
				}
			}

			return;
		}
		if (C[Index] == '?')
		{
			for (int j = 0; j <= 9; ++j)
			{
				char c1 = C[Index];

				C[Index] = '0' + j;
				dfs(pos + 1, C, J);
				C[Index] = c1;
			}
			
			return;
		}

		if (J[Index] == '?')
		{
			for (int j = 0; j <= 9; ++j)
			{
				char c1 = J[Index];

				J[Index] = '0' + j;
				dfs(pos + 1, C, J);
				J[Index] = c1;

			}
			return;
		}
		dfs(pos + 1, C, J);
	}
	else
	{
		auto nC = std::stoll(C);
		auto nJ = std::stoll(J);

		if (abs(nC - nJ) == minDiff)
		{
			if ((nC == rC))
			{
				if (nJ < rJ)
				{
					minDiff = abs(nC - nJ);
					resultC = C;
					resultJ = J;

					rC = nC;
					rJ = nJ;
				}
			}

			if (nC < rC)
			{
				minDiff = abs(nC - nJ);
				resultC = C;
				resultJ = J;

				rC = nC;
				rJ = nJ;
			}
		}

		if (abs(nC - nJ) < minDiff)
		{
			minDiff = abs(nC - nJ);
			resultC = C;
			resultJ = J;

			rC = nC;
			rJ = nJ;
		}
			
	}
}

void solve(int testNr)
{
	minDiff = numeric_limits<long long>::max();
	string C, J;
	inFile >> C >> J;
	dfs(1, C, J);
	outFile << "Case #" << testNr << ": " << resultC << " " << resultJ << endl;
}

int main()
{
	int numTests;

	inFile.open("test.in", ios::in);
	outFile.open("test.out", ios::out);
	inFile >> numTests;
	for (int i = 0; i < numTests; ++i)
	{
		solve(i + 1);
	}
	inFile.close();
	outFile.close();
	return 0;
}