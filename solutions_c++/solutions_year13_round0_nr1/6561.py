
#include <algorithm>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 

void solve(VS field)
{
	REP(i, 4)
	{
		bool x_win = true;
		REP(j, 4)
		{
			x_win &= (field[i][j] == 'X' || field[i][j] == 'T');
		}

		if (x_win)
		{
			cout << "X won\n";
			return;
		}
	}

	REP(i, 4)
	{
		bool x_win = true;
		REP(j, 4)
		{
			x_win &= (field[j][i] == 'X' || field[j][i] == 'T');
		}

		if (x_win)
		{
			cout << "X won\n";
			return;
		}
	}

	int x = 0, y = 0;
	bool x_win = true;
	REP(i, 4)
	{
		x_win &= (field[x][y] == 'X' || field[x][y] == 'T');
		x++;
		y++;
	}

	if (x_win)
	{
		cout << "X won\n";
		return;
	}


	x = 0, y = 3;
	x_win = true;
	REP(i, 4)
	{
		x_win &= (field[x][y] == 'X' || field[x][y] == 'T');
		x++;
		y--;
	}

	if (x_win)
	{
		cout << "X won\n";
		return;
	}


	////


	REP(i, 4)
	{
		bool o_win = true;
		REP(j, 4)
		{
			o_win &= (field[i][j] == 'O' || field[i][j] == 'T');
		}

		if (o_win)
		{
			cout << "O won\n";
			return;
		}
	}

	REP(i, 4)
	{
		bool o_win = true;
		REP(j, 4)
		{
			o_win &= (field[j][i] == 'O' || field[j][i] == 'T');
		}

		if (o_win)
		{
			cout << "O won\n";
			return;
		}
	}

	x = 0, y = 0;
	bool o_win = true;
	REP(i, 4)
	{
		o_win &= (field[x][y] == 'O' || field[x][y] == 'T');
		x++;
		y++;
	}

	if (o_win)
	{
		cout << "O won\n";
		return;
	}


	x = 0, y = 3;
	o_win = true;
	REP(i, 4)
	{
		o_win &= (field[x][y] == 'O' || field[x][y] == 'T');
		x++;
		y--;
	}

	if (o_win)
	{
		cout << "O won\n";
		return;
	}

	bool can_move = false;

	REP(i, 4)
	{
		REP(j, 4)
		{
			if (field[i][j] == '.')
				can_move = true;
		}
	}


	if (can_move)
	{
		cout << "Game has not completed\n";
	}
	else
	{
		cout << "Draw\n";
	}




}

int main(int argc, char* argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	string str;
	getline(cin, str);
	int T;
	sscanf(str.c_str(), "%d", &T);


	REP(i, T)
	{
		VS field;
		REP(j, 4)
		{
			getline(cin, str);
			field.push_back(str);
		}


		cout << "Case #" << (i+1) << ": ";
		solve(field);


		getline(cin, str);

	}






}