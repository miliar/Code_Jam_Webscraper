#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

bool impossible(vector<string> &grid, int r, int c)
{
	int ii=grid.size(), jj=grid[0].size();

	//possible.
	if(grid[r][c]=='.')
		return false;

	for(int i=0; i<ii; i++)
	{
		if(i==r)
			continue;
		if(grid[i][c]!='.')
			return false;
	}

	for(int j=0; j<jj; j++)
	{
		if(j==c)
			continue;
		if(grid[r][j]!='.')
			return false;
	}

	return true;
}

int main()
{
	int tt, ti;
	fin >> tt;

	for(ti=1; ti<=tt; ti++)
	{
		fout << "Case #" << ti << ": ";
		////////////////////////////////////////////////////

		vector<string> grid;
		int r, c;
		bool imp;

		fin >> r >> c;
		grid.resize(r);

		for(int i=0; i<r; i++)
			fin >> grid[i];

		imp = false;
		for(int i=0; i<r; i++)
			for(int j=0; j<c; j++)
			{
				if(impossible(grid, i, j))
				{
					imp=true;
					i=r;
					j=c;
				}
			}

		if(imp)
		{
			fout << "IMPOSSIBLE" << endl;
			continue;
		}

		int ans=0;

		//up edge
		for(int i=0; i<c; i++)
		{
			for(int j=0; j<r; j++)
			{
				if(grid[j][i]!='.')
				{
					if(grid[j][i]=='^')
						ans++;
					break;
				}
			}
		}

		//right
		for(int i=0; i<r; i++)
		{
			for(int j=c-1; j>=0; j--)
			{
				if(grid[i][j]!='.')
				{
					if(grid[i][j]=='>')
						ans++;
					break;
				}
			}
		}

		//bottom
		for(int i=0; i<c; i++)
		{
			for(int j=r-1; j>=0; j--)
			{
				if(grid[j][i]!='.')
				{
					if(grid[j][i]=='v')
						ans++;
					break;
				}
			}
		}

		//left
		for(int i=0; i<r; i++)
		{
			for(int j=0; j<c; j++)
			{
				if(grid[i][j]!='.')
				{
					if(grid[i][j]=='<')
						ans++;
					break;
				}
			}
		}

		fout << ans << endl;
	}

	return 0;
}