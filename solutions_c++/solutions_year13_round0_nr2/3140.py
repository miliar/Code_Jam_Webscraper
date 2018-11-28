#include <iostream>
#include <fstream>

using namespace std;

bool solve(int** lawn, int n, int m);

int main()
{
	int T;
	char strBuff[405];
	int n, m;
	int** lawn;


	ifstream fin;
	fin.open("B.txt", ifstream::in);

	ofstream fout;
	fout.open("Output.txt", ofstream::out);

	fin.getline(strBuff, 6);

	sscanf(strBuff, "%d", &T);

	for (int i = 0; i < T; i++)
	{
		fout << "Case #" << (i+1) << ": ";
		cout << "Case (i+1)\n";

		fin >> n;
		fin >> m;

		lawn = new int*[n];
		for (int j = 0; j < n; j++)
		{
			lawn[j] = new int[m];
		}

		for (int j = 0; j < n; j++)
		{
			fin >> lawn[j][0];

			for (int k = 1; k < m; k++)
			{
				fin >> lawn[j][k];
			}

		}
		cout << "\n";
		if (solve(lawn, n, m)) fout << "YES\n";
		else fout << "NO\n";
		
		for (int j = 0; j < n; j++)
		{
			delete[] lawn[j];
		}
		delete[] lawn;
	}
	fout.close();
	
	fin.close();
}

bool solve(int** lawn, int n, int m)
{
	int* rowMax = new int[n];
	int* colMax = new int[m];
	for (int i = 0; i < n; i++)
	{
		rowMax[i] = lawn[i][0];
	}
	for (int j = 0; j < m; j++)
	{
		colMax[j] = lawn[0][j];
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (rowMax[i] < lawn[i][j]) rowMax[i] = lawn[i][j];
			if (colMax[j] < lawn[i][j]) colMax[j] = lawn[i][j];
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (lawn[i][j] < rowMax[i] && lawn[i][j] < colMax[j]) return false;
		}
	}
	return true;
}
