#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int n, m;
int map[100][100], a[100][100];
bool judge()
{
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
		{
			a[i][j] = 100;
		}
	int max;
	for (int i=0; i<n; i++)
	{
		max = 0;
		for (int j=0; j<m; j++)
		{
			if (map[i][j] > max) max = map[i][j];
		}
		for (int j=0; j<m; j++)
		{
			if (a[i][j] > max) a[i][j] = max;
		}
	}
	for (int j=0; j<m; j++)
	{
		max = 0;
		for (int i=0; i<n; i++)
		{
			if (map[i][j] > max) max = map[i][j];
		}
		for (int i=0; i<n; i++)
		{
			if (a[i][j] > max) a[i][j] = max;
		}
	}
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<m; j++)
		{
			if (a[i][j] != map[i][j])
			{
				return false;
			}
		}
	}
	return true;
}
int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for (int i=0; i<t; i++)
	{
		memset(map, 0, sizeof(map));
		fin >> n >> m;
		for (int j=0; j<n; j++)
		{
			for (int k=0; k<m; k++)
			{
				fin >> map[j][k];
			}
		}
		fout << "Case #" << i+1 << ": ";
		if (judge())
		{
			fout << "YES" << endl;
		}
		else
		{
			fout << "NO" << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}
