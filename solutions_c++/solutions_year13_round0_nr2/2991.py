
#include <cstdio>
#include <cstdlib>
#include <iostream>

#define forl(i,a,b) for(int i = a; i < b; ++i)

using namespace std;

int board[101][101];

int crowmax[101];
int ccolmax[101];

int colmax(int w, int h, int col)
{
	int _min = board[col][0];
	int _max = board[col][0];
	forl(j,0,h)
	{
		if (_min > board[col][j]) _min = board[col][j];
		if (_max < board[col][j]) _max = board[col][j];
	}
	return (_max);
}

int rowmax(int w, int h, int row)
{
	int _min = board[0][row];
	int _max = board[0][row];
	forl(j,0,w)
	{
		if (_min > board[j][row]) _min = board[j][row];
		if (_max < board[j][row]) _max = board[j][row];
	}
	return (_max);
}

int main(int argc, char **argv)
{
	int t;
	cin >> t;
	forl(test,1,t+1)
	{
		int w,h;
		cin >> h >> w;
		bool valid = true;
		forl(y,0,h)
		{
			forl(x,0,w)
			{
				cin >> board[x][y];
			}
		}

		forl(y,0,h)
		{
			crowmax[y] = rowmax(w,h,y);
		}
		forl(x,0,w)
		{
			ccolmax[x] = colmax(w,h,x);
		}

		forl(y,0,h)
		{
			forl(x,0,w)
			{
				int b = board[x][y];
				if (b < ccolmax[x] && b < crowmax[y])
				{
					valid = false;
					break;
				}
			}
			if (!valid)
				break;
		}
		if (valid)
		{
			cout << "Case #" << test << ": YES" << endl;
		}
		else
		{

			cout << "Case #" << test << ": NO" << endl;
		}
		
	}
	return 0;
}
