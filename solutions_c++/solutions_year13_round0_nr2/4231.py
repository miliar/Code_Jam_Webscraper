/*
 * lawnmower.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Matt
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int check_vert(vector<vector<int> > a, int num_rows, int x, int y)
{
	int flag = 1;
	for(int i=0; i<num_rows; i++)
	{
		if(i != y && a[i][x] > a[y][x])
		{
			flag = 0;
			return flag;
		}
	}

	return flag;
}

int check_horiz(vector<vector<int> > a, int num_cols, int x, int y)
{
	int flag = 1;
	for(int j=0; j<num_cols; j++)
	{
		if(j != x && a[y][j] > a[y][x])
		{
			flag = 0;
			return flag;
		}
	}

	return flag;
}

int check_pixels(vector<vector<int> > a, int N, int M)
{
	for(int x=0; x<M; x++)
	{
		for(int y=0; y<N; y++)
		{
			if(check_vert(a, N, x, y) == 0)
			{
				if(check_horiz(a, M, x, y) == 0)
				{
					return 0;
				}
			}
		}
	}

	return 1;
}

int main()
{
	ofstream out;
	out.open("answer_large.txt");

	int num_cases;
	cin >> num_cases;

	for(int i=1; i<=num_cases; i++)
	{
		int N, M;
		cin >> N; cin >> M;

		vector<vector<int> > a(N, vector<int>(M));
		for(int y=0; y<N; y++)
		{
			for(int x=0; x<M; x++)
			{
				int n;
				cin >> n;	//a[y][x] gives the yth row and xth column of a
				a[y][x] = n;
			}
		}

		int flag = check_pixels(a, N, M);

		out << "Case #" << i << ": ";

		if(flag == 1)
		{
			out << "YES" << endl;
		}
		else
		{
			out << "NO" << endl;
		}
	}

	out.close();
}

