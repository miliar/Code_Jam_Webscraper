#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

const int SIZE = 4;
vector<vector<char> > board(SIZE);
char symbol;

void solve();
bool checkRow(int i);
bool checkCol(int i);
bool checkDiags();

int main()
{
    for(int i=0; i<SIZE; ++i)
    {
	board[i].resize(SIZE);
    }

    int T;
    cin >> T;

    for(int i=1; i<=T; ++i)
    {
	cout << "Case #" << i << ": ";
	solve();
    }

    return 0;
}


void solve()
{
    for(int i=0; i<SIZE; ++i)
    {
	for(int j=0; j<SIZE; ++j)
	{
	    cin >> board[i][j];
	}
    }

    for(int i=0; i<SIZE; ++i)
    {
	if(checkRow(i))
	{
	    cout << symbol << " won" << endl;
	    return;
	}
	if(checkCol(i))
	{
	    cout << symbol << " won" << endl;
	    return;
	}
    }

    if(checkDiags())
    {
	cout << symbol << " won" << endl;
	return;
    }

    for(int i=0; i<SIZE; ++i)
    {
	for(int j=0; j<SIZE; ++j)
	{
	    if(board[i][j] == '.')
	    {
		cout << "Game has not completed" << endl;
		return;
	    }
	}
    }

    cout << "Draw" << endl;
}


bool checkRow(int i)
{
    if(board[i][0] != 'T')
    {
	symbol = board[i][0];
    }
    else
    {
	symbol = board[i][1];
    }

    if(symbol == '.')
    {
	return false;
    }

    for(int j=1; j<SIZE; ++j)
    {
	if(board[i][j] != symbol && board[i][j] != 'T')
	{
	    return false;
	}
    }

    return true;
}

bool checkCol(int i)
{
    if(board[0][i] != 'T')
    {
	symbol = board[0][i];
    }
    else
    {
	symbol = board[1][i];
    }

    if(symbol == '.')
    {
	return false;
    }

    for(int j=1; j<SIZE; ++j)
    {
	if(board[j][i] != symbol && board[j][i] != 'T')
	{
	    return false;
	}
    }

    return true;
}

bool checkDiags()
{
    bool won = true;
    if(board[0][0] != 'T')
    {
	symbol = board[0][0];
    }
    else
    {
	symbol = board[1][1];
    }

    if(symbol == '.')
    {
	won = false;
    }

    for(int j=1; j<SIZE; ++j)
    {
	if(board[j][j] != symbol && board[j][j] != 'T')
	{
	    won = false;
	}
    }

    if(won)
    {
	return true;
    }

    if(board[SIZE-1][0] != 'T')
    {
	symbol = board[SIZE-1][0];
    }
    else
    {
	symbol = board[SIZE-2][1];
    }

    if(symbol == '.')
    {
	return false;
    }

    for(int j=1; j<SIZE; ++j)
    {
	if(board[SIZE-j-1][j] != symbol && board[SIZE-j-1][j] != 'T')
	{
	    return false;
	}
    }

    return true;
}
