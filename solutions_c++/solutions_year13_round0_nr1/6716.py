#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

bool the_winner_is(char c , vector<string> &V)
{
	int won_diagonal1 = 1 , won_diagonal2 = 1;
	for(int i = 0; i < 4; ++i)
	{
		int won_horizontal = 1 , won_vertical = 1;
		for(int j = 0; j < 4; ++j)
		{
			if(V[i][j] != c && V[i][j] != 'T')
				won_horizontal = 0;
			if(V[j][i] != c && V[j][i] != 'T')
			{
				won_vertical = 0;
			}
		}
		if(won_horizontal || won_vertical)return true;
		
		if(V[i][i] != c && V[i][i] != 'T')
			won_diagonal1 = 0;
		if(V[i][3-i] != c && V[i][3-i] != 'T')
			won_diagonal2 = 0;
	}
	return won_diagonal1 || won_diagonal2;
}

int main()
{
	int T;
	cin >> T;
	for(int tc = 1 ; tc<=T ; ++tc)
	{
		vector<string> V(4);
		int finished = 1;
		for(int i = 0; i < 4; ++i)
		{
			cin >> V[i];
			for(int j = 0; j < 4; ++j)
				if(V[i][j]=='.')
					finished = 0;
		}
		cout << "Case #" << tc << ": ";
		if( the_winner_is('O',V) ) cout << "O won" << endl;
		else if( the_winner_is('X',V) ) cout << "X won" << endl;
		else if( finished ) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;
	}
	
}
/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O


*/

