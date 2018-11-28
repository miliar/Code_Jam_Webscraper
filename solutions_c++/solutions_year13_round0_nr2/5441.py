/*
 * main.cpp
 *
 *  Created on: 2013-4-13
 *      Author: chenjd
 */

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int grass[10][10];
	int T;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin >> T;

	int test_case;
	for (test_case = 1; test_case <= T; test_case++)
	{
		int n, m;
		int num_height[101] = { 0 };
		int next[101];
		int pre = 0;

		bool noflag = false;
		fin >> n >> m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				fin >> grass[i][j];
				num_height[grass[i][j]]++;
			}
		for (int i = 1; i <= 100; i++)
		{
			if (num_height[i] != 0)
			{
				next[pre] = i;
				pre = i;
			}
		}
		next[pre] = -1;


		int i, j;
		int shortest = next[0];
		while (!noflag && num_height[shortest] != n * m)
		{
			int subscript_col[10], subscript_row[10];
			int num_min_row = 0, num_min_col = 0;
			for ( i = 0; i < n; i++)
			{
				if (grass[i][0] == shortest)
				{
					for (  j = 0; j < m; j++)
					{
						if (grass[i][j] != shortest)
							break;
					}
					if(j == m)
					subscript_row[num_min_row++] = i;
				}
			}
			for (  j = 0; j < m; j++)
			{
				if (grass[0][j] == shortest)
				{
					for (  i = 0; i < n; i++)
					{
						if (grass[i][j] != shortest)
							break;
					}
					if(i == n)
					subscript_col[num_min_col++] = j;
				}
			}
			for (int min_row = 0; min_row < num_min_row; min_row++)
			{
				for (  j = 0; j < m; j++)
				{
					if (grass[subscript_row[min_row]][j] == shortest)
					{
						grass[subscript_row[min_row]][j] = next[shortest];
						num_height[shortest]--;
						num_height[next[shortest]]++;
					}
				}
			}
			for (int min_col = 0; min_col < num_min_col; min_col++)
			{
				for (  i = 0; i < n; i++)
				{
					if (grass[i][subscript_col[min_col]] == shortest)
					{
						grass[i][subscript_col[min_col]] = next[shortest];
						num_height[shortest]--;
						num_height[next[shortest]]++;
					}
				}
			}
			if (num_height[shortest] != 0)
			{
				fout << "Case #" << test_case << ": NO" << endl;
				noflag = true;
				break;
			}
			shortest = next[shortest];
		}
		if (!noflag)
			fout << "Case #" << test_case << ": YES" << endl;


	}
	return 0;
}
