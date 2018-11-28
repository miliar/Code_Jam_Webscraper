#include <iostream>

using namespace std;

char board[4][4];
bool draw = true;

void getInput()
{
	for(int y = 0; y < 4; y++)
	{
		for(int x = 0; x < 4; x++)
		{
			char temp = cin.get();
			if(temp == '.')
				draw = false;
			board[y][x] = temp;
		}
		cin.ignore(256, '\n');
	}
	cin.ignore(256, '\n');
}

void printBoard()
{
	for(int y = 0; y < 4; y++)
	{
		for(int x = 0; x < 4; x++)
		{
			cout << board[y][x];
		}
		cout << endl;
	}
	cout << endl;
}

int checkRow(int y) // 0: No win, 1: X wins, 2: O wins
{
	short circles = 0, crosses = 0;
	short t = 0;
	for(int x = 0; x < 4; x++)
	{
		if(board[y][x] == 'X')
			crosses++;
		if(board[y][x] == 'O')
			circles++;
		if(board[y][x] == 'T')
			t++;
	}
	if(crosses == 4 || crosses + t == 4)
		return 1;
	if(circles == 4 || circles + t == 4)
		return 2;
	return 0;
}

int checkColumn(int x)
{
	short circles = 0, crosses = 0;
	short t = 0;
	for(int y = 0; y < 4; y++)
	{
		if(board[y][x] == 'X')
			crosses++;
		if(board[y][x] == 'O')
			circles++;
		if(board[y][x] == 'T')
			t++;
	}
	if(crosses == 4 || crosses + t == 4)
		return 1;
	if(circles == 4 || circles + t == 4)
		return 2;
	return 0;
}

int checkDiags()
{
	short circles = 0, crosses = 0;
	short t = 0;
	int y = 0, x = 0;
	while(y < 4 && x < 4)
	{
		if(board[y][x] == 'X')
			crosses++;
		if(board[y][x] == 'O')
			circles++;
		if(board[y][x] == 'T')
			t++;
		y++;
		x++;
	}
	if(crosses == 4 || crosses + t == 4)
		return 1;
	if(circles == 4 || circles + t == 4)
		return 2;
	
	crosses = 0;
	circles = 0;
	t = 0;
	y = 0, x = 3;
	while(y < 4 && x >= 0)
	{
		if(board[y][x] == 'X')
			crosses++;
		if(board[y][x] == 'O')
			circles++;
		if(board[y][x] == 'T')
			t++;
		y++;
		x--;
	}
	if(crosses == 4 || crosses + t == 4)
		return 1;
	if(circles == 4 || circles + t == 4)
		return 2;
	return 0;
}

int main() 
{
	int cases = 0;
	cin >> cases;
	cin.ignore(256, '\n');
	
	for(int i = 1; i <= cases; i++)
	{
		draw = true;
		getInput();
		int winner = 0;
		for(int i = 0; i < 4; i++)
		{
			winner = checkColumn(i);
			if(winner != 0)
				break;
			winner = checkRow(i);
			if(winner != 0)
				break;
		}
		if(winner == 0)
		{
			winner = checkDiags();
		}
		
		cout << "Case #" << i << ": ";
		if(winner == 1)
			cout << "X won" << endl;
		else if(winner == 2)
			cout << "O won" << endl;
		else if(winner == 0 && draw)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
		// printBoard();
	}	
}
