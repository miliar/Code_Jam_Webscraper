#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>

using namespace std;

static ifstream fi;
static ofstream fo;

void redirectInput(const std::string& fileName)
{
	fi.open(fileName, std::ios_base::in);
	std::cin.rdbuf(fi.rdbuf());
}

void redirectOutput(const std::string& fileName)
{
	fo.open(fileName, std::ios_base::out);
	std::cout.rdbuf(fo.rdbuf());
}

enum GameState
{
	ePlaying,
	eYes,
	eNo,
	eDraw,
};

bool checkRow(int l[100][100], int n, int m, int i, int maxVal);
bool checkCol(int l[100][100], int n, int m, int j, int maxVal);

bool checkCol(int l[100][100], int n, int m, int j, int maxVal)
{
	int i;

	//Verify max limit
	for (i = 0; i < n; ++i)
	{
		if (l[i][j] > maxVal)
			return false;
	}

	//Recurse lower values
	for (i = 0; i < n; ++i)
	{
		if (l[i][j] < maxVal && !checkRow(l, n, m, i, l[i][j]))
			return false;
	}
	
	return true;
}

bool checkRow(int l[100][100], int n, int m, int i, int maxVal)
{
	int j;

	//Verify max limit
	for (j = 0; j < m; ++j)
	{
		if (l[i][j] > maxVal)
			return false;
	}

	//Recurse lower values
	for (j = 0; j < m; ++j)
	{
		if (l[i][j] < maxVal && !checkCol(l, n, m, j, l[i][j]))
			return false;
	}

	return true;
}

void main()
{
	redirectInput("in.txt");
	redirectOutput("out.txt");

	int caseCount;
	std::string str;
	int i,j,k;
	int n,m;

	int l[100][100];
	bool bOk;
	int maxRowVal;

	cin >> caseCount;
	cin.get();

	if (caseCount < 1 || caseCount > 100)
		return;

	for (i = 0; i < caseCount; ++i)
	{
		cin >> n;
		cin.get();
		cin >> m;

		// Lawn pattern loading
		for (j = 0; j < n; ++j)
		{
			for (k = 0; k < m; ++k)
				cin >> l[j][k];
			cin.get();
		}
		
		bOk = true;

		// Solving
		for (j = 0; j < n; ++j)
		{
			// Compute max row val
			maxRowVal = l[j][0];

			for (k = 0; k < m; ++k)
			{
				if (l[j][k] > maxRowVal)
					maxRowVal = l[j][k];
			}
		
			// Solve
			bOk = checkRow(l, n, m, j, maxRowVal);

			if (!bOk)
				break;
		}
	
		cout << "Case #" << (i + 1) << ": ";
		if (bOk)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}
