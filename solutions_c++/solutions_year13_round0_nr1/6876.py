#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

string getOutcome(string);
bool caseHasOpening(int, string);

const int WIN_CASES = 10;
int WIN_STATES[WIN_CASES][4] = {
	{0, 1, 2, 3},
	{4, 5, 6, 7},
	{8, 9, 10, 11},
	{12, 13, 14, 15},
	{0, 4, 8, 12},
	{1, 5, 9, 13},
	{2, 6, 10, 14},
	{3, 7, 11, 15},
	{0, 5, 10, 15},
	{3, 6, 9, 12}
};

int main()
{
	int cases;
	// File in initialization
	string path = "A-large.in";
	string outputPath = "output-large0.txt";
	ifstream inputFile;
	inputFile.open(path);
	// Get number of cases
	inputFile >> cases;

	string* boards = new string[cases];

	for (int i = 0; i < cases; i++)
	{
		string totalInput = "";
		char disregarded;
		for (int j = 0; j < 4; j++)
		{
			string input;
			inputFile >> input;
			totalInput += input;
		}
		inputFile.get(disregarded);
		boards[i] = totalInput;
	}

	string outcomes = "";
	for (int i = 0; i < cases; i++)
	{

		outcomes += "Case #" + to_string(static_cast<long long>(i + 1)) + ": ";
		outcomes += getOutcome(boards[i]);
		outcomes += "\n";
	}

	ofstream outputFile;
	outputFile.open(outputPath);
	outputFile << outcomes;
	return 0;
}

string getOutcome(string input)
{
	bool won = false;
	char winner;
	bool openings = false;
	for (int i = 0; i < WIN_CASES; i++)
	{
		if (won)
		{
			break;
		}
		char player;
		if (caseHasOpening(i, input))
		{
			openings = true;
			continue;
		}
		int jStart = 1;
		char initialInput = input[WIN_STATES[i][0]];
		if (initialInput == 'T')
		{
			initialInput = input[WIN_STATES[i][1]];
			player = initialInput;
			jStart += 1;
		}
		else
		{
			player = initialInput;
		}
		for (int j = jStart; j < 4; j++)
		{
			char in = input[WIN_STATES[i][j]];
			if ((in == player) || (in == 'T'))
			{
				if (j == 3)
				{
					winner = player;
					won = true;
				}
			}
			else
			{
				break;
			}
		}
	}
	
	if (won)
	{
		string winnerString = "";
		winnerString.push_back(winner);
		return winnerString + " won";
	}
	else if (!openings)
	{
		return "Draw";
	}
	else
	{
		return "Game has not completed";
	}
}

bool caseHasOpening(int n, string board)
{
	for (int i = 0; i < 4; i++)
	{
		if (board[WIN_STATES[n][i]] == '.')
		{
			return true;
		}
	}
	return false;
}