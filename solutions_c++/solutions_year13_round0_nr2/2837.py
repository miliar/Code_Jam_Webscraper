// GCJ2013QualifierBAttempt2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

inline bool WasThisSquarePossiblyMowedFromAHorizontalDirectionP(const int i, const int j, const vector<vector<int>> RectangularLawn) {
	for (int temp = 0; (unsigned int)temp < RectangularLawn[0].size(); ++temp) {
		if (RectangularLawn[i][j] < RectangularLawn[i][temp]) {
			return false;
		}
	}

	return true;
}

inline bool WasThisSquarePossiblyMowedFromAVerticalDirectionP(const int i, const int j, const vector<vector<int>> RectangularLawn) {
	for (int temp = 0; (unsigned int)temp < RectangularLawn.size(); ++temp) {
		if (RectangularLawn[i][j] < RectangularLawn[temp][j]) {
			return false;
		}
	}

	return true;
}

inline bool GetSolution(const vector<vector<int>>& RectangularLawn)
{
	for (unsigned int i = 0; i < RectangularLawn.size(); ++i) {
		for (unsigned int j = 0; j < RectangularLawn[0].size(); ++j)
		{
			if (!WasThisSquarePossiblyMowedFromAHorizontalDirectionP(i,j,RectangularLawn) &&
				!WasThisSquarePossiblyMowedFromAVerticalDirectionP(i,j,RectangularLawn)) {
					return false;
			}
		}
	}

	return true;
}

inline vector<vector<int>> GetInput(const int a, const int b) {
	vector<vector<int>> RectangularLawn = vector<vector<int>>();

	for (int i = 0; i < a; ++i) {
		vector<int> HorizontalLawnStrip = vector<int>();

		for (int j = 0; j < b; ++j) {
			int temp;
			cin >> temp;
			HorizontalLawnStrip.push_back(temp);
		}

		RectangularLawn.push_back(HorizontalLawnStrip);
	}

	return RectangularLawn;
}

inline string getInputAndSolution(const int a, const int b) {
	return GetSolution(GetInput(a,b)) ? "YES" : "NO";
}

int _tmain(int argc, _TCHAR* argv[])
{
	ios::sync_with_stdio(0);
#pragma warning(disable : 4996)
	freopen("B-small-attempt8.in", "r", stdin);
#pragma warning(disable : 4996)
	freopen("b8.out", "w", stdout);

	int numberOfTestCases;
	cin >> numberOfTestCases;

	for (int z = 0; z < numberOfTestCases; ++z) {
		int a;
		int b;
		cin.ignore(1);
		cin >> a;
		cin >> b;

		string temp = getInputAndSolution(a,b);
		cout << "Case #" << (z + 1) << ": " << temp << endl;
	}

	return 0;
}

