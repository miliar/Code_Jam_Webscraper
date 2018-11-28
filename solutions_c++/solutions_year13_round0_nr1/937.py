#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
#include<cmath>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>
using namespace std;

// board: -1 if not filled, 0 if O, 1 if T, 2 if X
// return: 0 if O, 1 if X, 2 if draw, 3 if not over
int game(vector<vector<int> > board)
{
	// status = 0 if filled, -1 if not
	int status = 0;

	// test rows
	for (int i = 0; i < 4; i++)
	{
		int sum = 0;
		for (int j = 0; j < 4; j++)
			if (board[i][j] < 0)
			{
				sum = -1;
				status = -1;
				break;
			}
			else
				sum += board[i][j];

		if (sum >= 7)
			return 1;
		else if (sum <= 1 && sum >= 0)
			return 0;
	}	
	
	// test columns
	for (int j = 0; j < 4; j++)
	{
		int sum = 0;
		for (int i = 0; i < 4; i++)
			if (board[i][j] < 0)
			{
				sum = -1;
				status = -1;
				break;
			}
			else
				sum += board[i][j];

		if (sum >= 7)
			return 1;
		else if (sum <= 1 && sum >= 0)
			return 0;
	}

	// test diagonal lines
	int sum = 0;
	for (int i = 0; i < 4; i++)
	{
		if (board[i][i] < 0)
		{
			sum = -1;
			status = -1;
			break;
		}
		else
			sum += board[i][i];
	}
	if (sum >= 7)
		return 1;
	else if (sum <= 1 && sum >= 0)
		return 0;
	sum = 0;
	for (int i = 0; i < 4; i++)
	{
		if (board[i][3-i] < 0)
		{
			sum = -1;
			status = -1;
			break;
		}
		else
			sum += board[i][3-i];
	}
	if (sum >= 7)
		return 1;
	else if (sum <= 1 && sum >= 0)
		return 0;

	if (status == -1)
		return 3;
	else
		return 2;
}

int main(int argv, char* argc)
{
	ifstream infile("test.txt");
	ofstream outfile("result.txt");
	if (!infile || !outfile)
	{
		cout << "wrong" << endl;
		return -1;
	}

	int numCase;
	infile >> numCase;
	
	string temp;
	getline(infile, temp);
//	char temp;
	for (int i = 0; i < numCase; i++)
	{
		vector<vector<int> > board;
		for (int j = 0; j < 4; j++)
		{
			vector<int> line;
			getline(infile, temp);
			for (int k = 0; k < 4; k++)
			{
				if (temp[k] == 'O')
					line.push_back(0);
				else if (temp[k] == 'X')
					line.push_back(2);
				else if (temp[k] == 'T')
					line.push_back(1);
				else
					line.push_back(-1);
			}
			board.push_back(line);
		}
		getline(infile, temp);

		int result = game(board);
				
		outfile << "Case #" << i+1 << ": ";
		if (result == 0)
			outfile << "O won" << endl;
		else if (result == 1)
			outfile << "X won" << endl;
		else if (result == 3)
			outfile << "Game has not completed" << endl;
		else
			outfile << "Draw" << endl;
	}

	infile.close();
	outfile.close();
}