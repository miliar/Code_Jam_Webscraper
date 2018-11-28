#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

/*
vector <int> vi;
vector <string> vstr;
queue <int > qi;
queue <string> qstr;
queue <int,int > qoi;
*/

int R, C;
char mapp[200][200] = { 0, };
vector <pair<int, int>> vii;


void printMapp()
{
	for (int i = 0; i < R+2; i++)
	{
		for (int j = 0; j < C+2; j++)
		{
			cout <<  mapp[i][j]<<"	";
		}
		cout << endl;
	}
	cout << endl;
}

int goStrat(int dir, int tx, int ty)
{
	int ttx = tx;
	int tty = ty;
	int ax, ay;
	if (dir == 1){ ax = 0; ay = 1; }
	if (dir == 2){ ax = 1; ay = 0; }
	if (dir == 3){ ax = 0; ay = -1; }
	if (dir == 4){ ax = -1; ay = 0; }

	while (1)
	{
		ttx += ax;
		tty += ay;
 
		if (mapp[ttx][tty] == -1)
			return -1;
		else if (mapp[ttx][tty] != '.')
		{
			return 1;
		}
	}
}

int isOK(int tx,int ty)
{
 
	int dir;
	if (mapp[tx][ty] == '.')	return 0;

	if (mapp[tx][ty] == '>')	dir = 1;
	else if (mapp[tx][ty] == 'v')	dir = 2;
	else if (mapp[tx][ty] == '<')	dir = 3;
	else if (mapp[tx][ty] == '^')	dir = 4;

	if (goStrat(dir, tx, ty) ==1 )
		return 0;
	else
	{
		if (dir != 1 && goStrat(1, tx, ty) == 1)	{ mapp[tx][ty] = '>';  return 1; }
		if (dir != 2 && goStrat(2, tx, ty) == 1){ mapp[tx][ty] = 'v'; return 1; }
		if (dir != 3 && goStrat(3, tx, ty) == 1){ mapp[tx][ty] = '<'; return 1; }
		if (dir != 4 && goStrat(4, tx, ty) == 1){ mapp[tx][ty] = '^'; return 1; }
	}

	return -1;
}


int main()
{
	freopen("input (1).txt", "r", stdin);
	freopen("output11.txt", "w", stdout);

	int nTestCase = 0;
	cin >> nTestCase;

	for (int iTestCase = 0; iTestCase < nTestCase; iTestCase++)
	{
		int tanswer, answer = 0;
		

		vii.clear();

		cin >> R >> C;
		memset(mapp, 0, sizeof(mapp));
		for (int i = 1; i <= R; i++)
		{
			for (int j = 1; j <= C; j++)
			{
				cin >> mapp[i][j];
			}
		}
		for (int i = 0; i <= R + 2; i++)
			mapp[i][0] = mapp[i][C + 1] = -1;
		for (int i = 0; i <= C + 2; i++)
			mapp[0][i] = mapp[R+1][i] = -1;

	//	printMapp();




		for (int i = 1; i <= R; i++)
		{
			for (int j = 1; j <= C; j++)
			{
				tanswer = isOK(i, j);
			//	cout << i << "," << j << " " << tanswer << endl;
				if (tanswer == -1)
				{
					answer = -1;
					break;
				}
				answer += tanswer;
			}
			if (tanswer == -1)
			{
				answer = -1;
				break;
			}
		}


		if (answer == -1)
			cout << "Case #" << iTestCase + 1
			<< ": " << "IMPOSSIBLE" << endl;
		else
		cout << "Case #" << iTestCase + 1
			<< ": " << answer<<endl;
	}
	return 0;
}