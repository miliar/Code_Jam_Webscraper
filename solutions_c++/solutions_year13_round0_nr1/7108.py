#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool contains_empty_space(string &line)
{
	for(int i = 0; i < 4; i++)
		if(line[i] == '.')
			return true;

	return false;
}

bool won_line(string &line, char c)
{
	for(int i = 0; i < 4; i++)
	{
		if(line[i] != c && line[i] != 'T')
			return false;
	}
	return true;
}

bool won_column(string *board, char c)
{
	
	for(int i = 0; i < 4; i++)
	{
		bool won = true;
		for(int j = 0; j < 4; j++)
			won = won && (board[j][i] == c  || board[j][i] == 'T');
		if(won)
			return true;
	}
	return false;
}

bool won_diagonal_line(string board[4], char c)
{
	return (   (board[0][0] == c || board[0][0] == 'T')
		&& (board[1][1] == c || board[1][1] == 'T')
		&& (board[2][2] == c || board[2][2] == 'T')
		&& (board[3][3] == c || board[3][3] == 'T') )
		|| 
		(  (board[0][3] == c || board[0][3] == 'T')
		&& (board[1][2] == c || board[1][2] == 'T')
		&& (board[2][1] == c || board[2][1] == 'T')
		&& (board[3][0] == c || board[3][0] == 'T') );
}

int main(int argc, char** argv)
{
	int numCases;
	string board[4];

	ofstream out("output.txt");
	ifstream in(argv[1]);
	
	in >> numCases;
	in >> ws;
	string temp;
	for(int i = 1; i <= numCases; i++)
	{
		bool x_won = false, o_won = false, found_empty_space = false;
		for(int j = 0; j < 4; j++)
		{
			getline(in, board[j]);
			
			x_won = x_won || won_line(board[j], 'X');
			o_won = o_won || won_line(board[j], 'O');
			found_empty_space = found_empty_space || contains_empty_space(board[j]);
		}

		getline(in, temp); // remove empty line

		x_won = x_won || won_diagonal_line(&board[0], 'X');
		o_won = o_won || won_diagonal_line(&board[0], 'O');

		x_won = x_won || won_column(&board[0], 'X');
		o_won = o_won || won_column(&board[0], 'O');

		if(x_won && o_won)
			out << "Case #" << i << ": " << "Draw" << endl;
		else if(x_won)
			out << "Case #" << i << ": " << "X won" << endl;
		else if(o_won)
			out << "Case #" << i << ": " << "O won" << endl;
		else if (found_empty_space)
			out << "Case #" << i << ": " << "Game has not completed" << endl;
		else
			out << "Case #" << i << ": " << "Draw" << endl;
	}
}