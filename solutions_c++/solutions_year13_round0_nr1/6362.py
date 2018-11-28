#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void load_board(vector< vector<char> > & board, bool & has_empty, ifstream & file)
{
	string line = "";

	for (int i = 0; i < 4; ++i)
	{
		file >> line;
		while (line.length() != 4)
			file >> line;

		for (int j = 0; j < 4; ++j)
		{
			if (line[j] == '.')
				has_empty = true;

			board[i][j] = line[j];
		}
	}
}

void print_board(vector< vector<char> > & board)
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cout << board[i][j];
		}
		cout << endl;
	}
}

bool symbol_same(char c1, char c2)
{
	if (c1 == '.')
		return false;
	if (c2 == '.')
		return false;

	return (c1 == c2 || c1 == 'T' || c2 == 'T');
}

bool vector_same(vector<char> & v)
{
	return symbol_same(v[0],v[1]) && symbol_same(v[0], v[2])
		&& symbol_same(v[0],v[3]) && symbol_same(v[1], v[2])
		&& symbol_same(v[1],v[3]) && symbol_same(v[2], v[3]);
}

char check_winner(vector< vector<char> > & board)
{
	for (int i = 0; i < 4; ++i)
	{
		vector<char> ivec (4);
		for (int j = 0; j < 4; ++j)
			ivec[j] = board[i][j];
	
		if (vector_same(ivec))
		{
			if (ivec[0] == 'T')
				return ivec[1];
			return ivec[0];
		}	
		
		vector<char> jvec (4);	
		for (int j = 0; j < 4; ++j)
			jvec[j] = board[j][i];
		
		if (vector_same(jvec))
		{
			if (jvec[0] == 'T')
				return jvec[1];
			return jvec[0];
		}
	}

	if (symbol_same(board[0][0], board[1][1]) &&
		symbol_same(board[0][0], board[2][2]) &&
		symbol_same(board[0][0], board[3][3]) &&
		symbol_same(board[1][1], board[2][2]) &&
		symbol_same(board[1][1], board[3][3]) &&
		symbol_same(board[2][2], board[3][3]))
	{
		if(board[0][0] == 'T')
			return board[1][1];
		return board[0][0];
	}

	if (symbol_same(board[0][3], board[1][2]) &&
		symbol_same(board[0][3], board[2][1]) &&
		symbol_same(board[0][3], board[3][0]) &&
		symbol_same(board[1][2], board[2][1]) &&
		symbol_same(board[1][2], board[3][0]) &&
		symbol_same(board[2][1], board[3][0]))
	{
		if(board[0][3] == 'T')
			return board[1][2];
		return board[0][3];
	}

	return 'd';
}

int main(int argc, char*argv[])
{

	ifstream file;
	file.open(argv[1]);

	int T;
	file >> T;

	bool has_empty_space = false;

	vector< vector<char> > board (4);
	for (int i = 0; i < 4; ++i)
		board[i].resize(4);
	
	for (int i = 0; i < T; ++i)
	{
		has_empty_space = false;
		load_board(board, has_empty_space, file);
		cout << "Case #" << i + 1 << ": ";
		
		char win = check_winner(board);
		if (win == 'd' && has_empty_space)
		{
			cout << "Game has not completed";
		}
		else if (win == 'd')
		{
			cout << "Draw";
		}
		else 
		{
			cout << win << " won";
		}
		cout << endl;
	}

	file.close();

	return 0;
}
