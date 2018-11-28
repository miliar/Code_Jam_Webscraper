#include "Lawnmower.h"

vector<vector<double>> Lawnmower::loadLawn(ifstream& in, int n, int m) const
{
	vector<vector<double>> result;
	result.resize(n);
	for (int i = 0; i < n; ++i)
	{
		result[i].resize(m);
		for (int j = 0; j < m; ++j)
		{
			in >> result[i][j];
		}
	}
	return result;
}

bool Lawnmower::checkLawnForPattern(const vector<vector<double>>& lawn) const
{
	for (int i = 0; i < lawn.size(); ++i)
	{
		for (int j = 0; j < lawn[0].size(); ++j)
		{
			if (!checkParticularElement(lawn,i,j))
				return false;
		}
	}
	return true;
}

bool Lawnmower::checkParticularElement(const vector<vector<double>>& lawn, int y, int x) const
{
	double elementToCheck = lawn[y][x];
	bool horizontalCheckPassed = true;
	bool verticalCheckPassed = true;
	// horizontal:
	for (int i = 0; i < lawn[0].size(); ++i)
	{
		if (lawn[y][i] > elementToCheck)
			horizontalCheckPassed = false;
	}
	// vertical:
	for (int i = 0; i < lawn.size(); ++i)
	{
		if (lawn[i][x] > elementToCheck)
			verticalCheckPassed = false;
	}
	return horizontalCheckPassed || verticalCheckPassed;
}

void Lawnmower::start(void)
{
	ifstream in(m_fileInput);
	ofstream out(m_fileOutput);

	int numberOfCases;
	in >> numberOfCases;
	for (int i = 1; i <= numberOfCases; ++i)
	{
		int N = 0, M = 0;
		in >> N >> M;
		vector<vector<double>> loan = loadLawn(in, N, M);
		if (checkLawnForPattern(loan))
			out << "Case #" << i << ": YES" << endl;
		else
			out << "Case #" << i << ": NO" << endl;
	}
}