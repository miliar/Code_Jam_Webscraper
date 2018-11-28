#include <iostream>
#include <fstream>
#include <string>

using namespace std;

enum State
{
	X_WON = 0,
	O_WON,
	DRAW,
	NOT_COMPLETE
};

State CheckLine(char line[4])
{
	int X = 0, O = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (line[i] == 'X')
			++X;
		else if (line[i] == 'O')
			++O;
		else if (line[i] == 'T')
		{	++X; ++O;}
		else
			return NOT_COMPLETE;
	}
	cout << X << " : " << O << " ";
	if (X == 4) return X_WON;
	else if (O == 4) return O_WON;
	else return DRAW;
}

State DetermineState(char board[4][4])
{
	char line[4];

	State state1;
	for (int j = 0; j < 4; ++j)
	{
		for (int i = 0; i < 4; ++i)
			line[i] = board[i][j];
		state1 = CheckLine(line);
		if (state1 == X_WON || state1 == O_WON)
			return state1;
	}

	State state2;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
			line[j] = board[i][j];
		state2 = CheckLine(line);
		if (state2 == X_WON || state2 == O_WON)
			return state2;
	}

	for (int i = 0, j = 0, k = 0; k < 4; ++i, ++j, ++k)
		line[k] = board[i][j];
	State state3 = CheckLine(line);
	if (state3 == X_WON || state3 == O_WON)
		return state3;

	for (int i = 0, j = 3, k = 0; k < 4; ++i, --j, ++k)
		line[k] = board[i][j];
	State state4 = CheckLine(line);
	if (state4 == X_WON || state4 == O_WON)
		return state4;

	if (state1 == DRAW || state2 == DRAW || state3 == DRAW || state4 == DRAW)
		return DRAW;
	else
		return NOT_COMPLETE;
}

int main()
{
	ifstream in_file("A-small-attempt1.in");
	ofstream out_file("out_file.txt");
	int test_cases = 0;

	string temp = "";
	getline(in_file, temp);
	test_cases = atoi(temp.c_str());

	for (int current_case = 0; current_case < test_cases; ++current_case)
	{
		char board[4][4];
		for (int j = 0; j < 4; ++j)
		{
			for (int i = 0; i < 4; ++i)
			{
				if (in_file.peek() == '\n')
					in_file.ignore();
				in_file >> board[i][j];
			}
		}
		State state = DetermineState(board);

		out_file << "Case #" << current_case + 1 << ": ";
		if (state == X_WON)
			out_file << "X won" << endl;
		else if (state == O_WON)
			out_file << "O won" << endl;
		else if (state == DRAW)
			out_file << "Draw" << endl;
		else 
			out_file << "Game has not completed" << endl;
		in_file.ignore();
	}

	out_file.close();
	in_file.close();
	cin.get();
	return 0;
}