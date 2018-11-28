#define _CRT_SECURE_NO_WARNINGS

#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

bool solve(const vector<string>& strings, int& numMoves)
{
	const size_t numStrings = strings.size();

	bool foundFirstChar = false;
	bool goodFirstChar = true;
	char firstChar;
	vector<int> firstCharCount;
	if (numStrings > 0)
		firstCharCount.resize(numStrings);
	int totalFirstCharCount = 0;

	for (int i = 0; i < numStrings; i++)
	{
		const string& curStr = strings[i];
		const size_t curStrSize = curStr.size();

		if (!curStr.empty())
		{
			if (!foundFirstChar)
			{
				if (i == 0)
				{
					firstChar = curStr.front();
					foundFirstChar = true;
				}
				else if (i > 0)
				{
					return false;
				}
			}

			for (int j = 0; j < curStrSize; j++)
			{
				if ((j == 0) && (curStr[0] != firstChar))
				{
					return false;
				}
				else if (curStr[j] == firstChar)
				{
					firstCharCount[i]++;
					totalFirstCharCount++;
				}
				else
				{
					break;
				}
			}
		}

		if (!goodFirstChar)
			return false;
	}

	vector<string> nextStrs;
	if (numStrings > 0)
	{
		const int avgFirstCharCount = totalFirstCharCount / numStrings;
		for (int i = 0; i < numStrings; i++)
		{
			numMoves += abs(firstCharCount[i] - avgFirstCharCount);
			const string& nextStr = strings[i].substr(firstCharCount[i]);
			if (!nextStr.empty())
			{
				nextStrs.push_back(nextStr);
			}
		}
	}

	return nextStrs.empty() || ((nextStrs.size() == numStrings) && solve(nextStrs, numMoves));
}

void solveCase(int caseNum)
{
	// Input
	vector<string> strings;
	int N;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		string nextStr;
		cin >> nextStr;
		strings.push_back(nextStr);
	}

	// Solve
	int numMoves = 0;
	const bool feglaWon = !solve(strings, numMoves);

	// Output
	cout << "Case #" << caseNum << ": ";
	if (feglaWon)
		cout << "Fegla Won";
	else
		cout << numMoves;
	
	cout << endl;
}

void main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		const int caseNum = i + 1;
		solveCase(caseNum);
	}
}
