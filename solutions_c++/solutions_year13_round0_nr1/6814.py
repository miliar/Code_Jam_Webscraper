/***********************************************************************************************************************
Author: Sagar Rakshe
Date: 13/04/2013
Problem Statement:  Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.

Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:

    "X won" (the game is over, and X won)
    "O won" (the game is over, and O won)
    "Draw" (the game is over, and it ended in a draw)
    "Game has not completed" (the game is not over yet)

If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.
Limits

The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above. 
***********************************************************************************************************************/
 
/*
-2 - '.'
-1 - mixed
0  - Null/Start
1  - 'X'
2  - 'O'
3  - 'T'

*/

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>

using namespace std;

char board[4][4];
int dot;

void win(char ch, int test)
{
	if(ch=='X')
		cout<<"Case #"<<test<<": X won"<<endl;
	else
		cout<<"Case #"<<test<<": O won"<<endl;
}

void solution(int test)
{
	int Xcount,Ocount,T,i,j;

	//Row Check		
	for (i = 0; i < 4; ++i)
	{
		Xcount=Ocount=T=0;		
		for (j = 0; j < 4; ++j)
		{
			if(board[i][j]=='X')
				Xcount++;
			else if(board[i][j]=='O')
				Ocount++;
			else if(board[i][j]=='T')
				T=1;
			else 
				break;
		}

		if((T==1 && Xcount==3) || (T==0 && Xcount==4))
		{
			win('X', test);
			return;
		}
			
		if((T==1 && Ocount==3) || (T==0 && Ocount==4))
		{
			win('O',test);
			return;
		}
	}
		
	
	//Column Check		
	for (i=0; i < 4; ++i)
	{
		Xcount=Ocount=T=0;		
		for (int j = 0; j < 4; ++j)
		{
			if(board[j][i]=='X')
				Xcount++;
			else if(board[j][i]=='O')
				Ocount++;
			else if(board[j][i]=='T')
				T=1;
			else
				break;
		}
		
		if((T==1 && Xcount==3) || (T==0 && Xcount==4))
		{
			win('X',test);
			return;
		}
			
		if((T==1 && Ocount==3) || (T==0 && Ocount==4))
		{
			win('O',test);
			return;
		}
	}

	Xcount=Ocount=T=0;	
	for (i=0,j=0; i < 4; ++i,++j)
	{	
		if(board[j][i]=='X')
				Xcount++;
		else if(board[j][i]=='O')
				Ocount++;
		else if(board[j][i]=='T')
				T=1;
		else
				break;

	}

	if((T==1 && Xcount==3) || (T==0 && Xcount==4))
	{
			win('X',test);
			return;
	}
			
	if((T==1 && Ocount==3) || (T==0 && Ocount==4))
	{
			win('O',test);
			return;
	}

	Xcount=Ocount=T=0;		
	for (i=0,j=3; i < 4; ++i,--j)
	{
		
		if(board[j][i]=='X')
				Xcount++;
		else if(board[j][i]=='O')
				Ocount++;
		else if(board[j][i]=='T')
				T=1;
		else
				break;

	}
	
	if((T==1 && Xcount==3) || (T==0 && Xcount==4))
	{
			win('X',test);
			return;
	}
			
	if((T==1 && Ocount==3) || (T==0 && Ocount==4))
	{
			win('O',test);
			return;
	}

	//Game not completed
	if(dot==0)
		cout<<"Case #"<<test<<": Draw"<<endl;

	//Draw
	else
		cout<<"Case #"<<test<<": Game has not completed"<<endl;

	//return;
}

int main(void)
{
	int test,temp;

	cin>>test;
	for(int k=1;k<=test;k++)
	{
		dot=0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				cin>>board[i][j];
				if(board[i][j]=='.')
					dot=1;
			}
		solution(k);
		//cin>>temp;
	}
		
	return 0;
}
