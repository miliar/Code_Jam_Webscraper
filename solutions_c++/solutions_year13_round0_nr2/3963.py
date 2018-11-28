#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

bool removeAll(vector< vector<int> > &lawn, int height, int count);
bool sameRow(const vector< vector<int> > &lawn, int row);
bool sameCol(const vector< vector<int> > &lawn, int col);

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B_large.out");

	int cases;
	fin >> cases;

	for (int i=0; i<cases; ++i)
	{
		int rows, cols;
		fin >> rows >> cols;

		vector< vector<int> > lawn(rows, vector<int>(cols));
		int heights[100];
		fill_n(heights, 100, 0);

		for (int a=0; a<rows; ++a)
		{
			for (int b=0; b<cols; ++b)
			{
				int temp;
				fin >> temp;
				lawn[a][b] = temp;
				++heights[temp-1];
			}
		}

		bool possible = true;
		for (int c=0; c<100; ++c)
		{
			if (heights[c])
			{
				if (!removeAll(lawn, c+1, heights[c]))
				{
					possible = false;
					break;
				}
			}
		}

		if (possible)
			fout << "Case #" << i+1 << ": YES" << endl;
		else
			fout << "Case #" << i+1 << ": NO" << endl;
	}

	return 0;
}

bool removeAll(vector< vector<int> > &lawn, int height, int count)
{
	for (int i=0; i<lawn.size(); ++i)
	{
		if (lawn[i][0] == height)
		{
			if (sameRow(lawn, i))
			{
				count -= lawn[i].size();
				lawn.erase(lawn.begin()+i);
				--i;
			}
		}
	}

	if (!lawn.empty())
	{
		for (int i=0; i<lawn[0].size(); ++i)
		{
			if (lawn[0][i] == height)
			{
				if (sameCol(lawn, i))
				{
					count -= lawn.size();
					for (int a=0; a<lawn.size(); ++a)
						lawn[a].erase(lawn[a].begin()+i);
					--i;
				}
			}
		}
	}

	if (count)
		return false;
	return true;
}

bool sameRow(const vector< vector<int> > &lawn, int row)
{
	int num = lawn[row][0];
	for (int i=1; i<lawn[row].size(); ++i)
	{
		if (lawn[row][i] != num)
			return false;
	}
	return true;
}
bool sameCol(const vector< vector<int> > &lawn, int col)
{
	int num = lawn[0][col];
	for (int i=1; i<lawn.size(); ++i)
	{
		if (lawn[i][col] != num)
			return false;
	}
	return true;
}