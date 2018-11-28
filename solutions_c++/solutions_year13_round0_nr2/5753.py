#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

string CheckYard(int test[10][10], int x, int y);
bool CheckRowCol(int test[][10], int i, int j, int x, int y);

int main()
{
	ifstream fin;
	fin.open ("input.txt");

	ofstream fout;
	fout.open ("output.txt");

	int N; // num test cases
	fin >> N;
	for( int n = 0; n < N; n++ ) {
		int yard[10][10];
		int X;
		int Y;
		fin >> X;
		fin >> Y;

		for(int i = 0; i < X; i++)
		{
			for(int j = 0; j < Y; j++)
			{
				fin >> yard[i][j];
			}
		}

		cout << "Case #" << n+1 << ": " << CheckYard(yard, X, Y) << endl;
		fout << "Case #" << n+1 << ": " << CheckYard(yard, X, Y) << endl;
	}
	return 0;
}
string CheckYard(int test[][10], int x, int y)
{
	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < y; j++)
		{
			if (test[i][j] == 1 && !CheckRowCol(test, i, j, x, y))
			{
				return "NO";
			}
		}
	}
	return "YES";
}

bool CheckRowCol(int test[][10], int i, int j, int x, int y)
{
	bool row = true;
	bool col = true;

	for (int b = 0; b < y; b++)
	{
		if (test[i][b] == 2)
		{
			row = false;
			break;
		}
	}

	for (int a = 0; a < x; a++)
	{
		if (test[a][j] == 2)
		{
			col = false;
			break;
		}
	}
	return row || col;
}