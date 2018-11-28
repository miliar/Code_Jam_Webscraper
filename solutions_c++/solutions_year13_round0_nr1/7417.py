#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

/*
	Problem

	Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares.
	There are two players: X and O. They take turns to make moves, with X starting.
	In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

	After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends.
	Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw.
	See the sample input for examples of various winning positions.

	Given an 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on.
	The statuses to choose from are:

		"X won" (the game is over, and X won)
		"O won" (the game is over, and O won)
		"Draw" (the game is over, and it ended in a draw)
		"Game has not completed" (the game is not over yet)

	Input

	The first line of the input gives the number of test cases, T. T test cases follow.
	Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.

	Output

	For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above.
	Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.

	Limits

	The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above. 


*/

char winner=' '; // X,O,D, I(ncomplete)


bool CheckLine(char line[4])
{	//Checks if some player completes a line
	
	char symbol=line[0];
	int i=0;
		
	if(symbol=='T')
	{	
		i++;
		symbol=line[i]	;
	}
	
	for(i;i<4;i++)
	{
		if(line[i]!=symbol && line[i]!='T')
			return false;
	}
	winner=symbol;
		
	return true;
}


int main(int argc, char *argv[]) {
	
	int numberOfCases;
	int linesRead=0; //Lines reads of a particular game
	char board[4][4];
	bool dot=false;//Indicates if there are a dot in the board
	string str;
	
	ofstream outputFile("A-large-output.in");
	
	ifstream inputFile("A-large.in");
	inputFile>>numberOfCases;
	
	for(int i=0;i<numberOfCases;i++)
	{
		outputFile<<"Case #"<<i+1<<": ";
		
		while(linesRead<4)
		{
			inputFile>>board[linesRead];
			
			str=board[linesRead];
			
			if(str.find('.')!=string::npos)
				dot=true;
			else
			{	
				CheckLine(board[linesRead]);//someone won
			}
			
			linesRead++;
		}
	
		if(winner==' ')
		{
			//Checks the columns
			char line[4]=" ";
			for(int j=0;j<4;j++)
			{
				line[0]=board[0][j];
				line[1]=board[1][j];
				line[2]=board[2][j];
				line[3]=board[3][j];
				
				str=line;
				if(str.find('.')!=string::npos)
					dot=true;
				else if(CheckLine(line))//someone won
					break;
			}
	
			//Check the diagonals
			line[0]=board[0][0];
			line[1]=board[1][1];
			line[2]=board[2][2];
			line[3]=board[3][3];
			
			str=line;
			if(str.find('.')!=string::npos)
				dot=true;
			else
				CheckLine(line);
				
			
			line[0]=board[0][3];
			line[1]=board[1][2];
			line[2]=board[2][1];
			line[3]=board[3][0];
			
			str=line;
			if(str.find('.')!=string::npos)
				dot=true;
			else
				CheckLine(line);
		}
		
		
		if(winner==' ')
		{
			if(dot)
				winner='I';
			else
				winner='D';			
		}
		
		
		switch(winner)
		{
		case 'X':outputFile<<"X won";break;	
		case 'O':outputFile<<"O won";break;	
		case 'D':outputFile<<"Draw";break;
		case 'I':outputFile<<"Game has not completed";break;	
		}
		
		linesRead=0;
		dot=false;
		winner=' ';		
		outputFile<<"\n";
	}
	
	return 0;
}
