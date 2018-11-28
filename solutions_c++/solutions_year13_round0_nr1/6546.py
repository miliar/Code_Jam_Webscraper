#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int board[4][4];

int GameStatus();

int main()
{
	string line;
	int index = 1;
	bool isInComplete = false;
	int numberOfTestCases = 0;
	ofstream outFile;
	ifstream inFile("A-large.in");
	outFile.open("A-large.out");

	if(inFile.is_open())
	{
		getline(inFile, line);
		
		numberOfTestCases = stoi(line);

		while(inFile.good())
		{
			for(int i=0;i < 4;i++)
			{
				getline(inFile, line);

				for(int j=0; j < 4; j++)
				{
					char piece = line[j];
					
					if(piece == '.')
					{
						board[i][j] = 0;
						isInComplete = true;
					}
					else if(piece == 'X')
					{
						board[i][j] = 2;
					}
					else if(piece == 'O')
					{
						board[i][j] = 1;
					}
					else 
					{
						board[i][j] = 3;
					}
				}
			}
			
			int state = GameStatus();

			switch(state)
			{
				case 0:
					if(isInComplete)
					{
						outFile << "Case #" << index << ": Game has not completed";
					}
					else
					{
						outFile << "Case #" << index << ": Draw";
					}

					break;

				case 1: 
					outFile << "Case #" << index << ": O won";

					break;

				case 2: 
					outFile << "Case #" << index << ": X won";

					break;
			}

			outFile << endl;

			index++;

			isInComplete = false;

			getline(inFile, line);
		}

		outFile.close();
	}

	return 0;
}

int GameStatus()
{
	int diagonalState = board[0][0];
	int secondDiagonalState = board[0][3];
	int rowState = 0;
	int colState = 0;

	for(int i=0;i < 4; i++)
	{
		diagonalState &= board[i][i];
		secondDiagonalState &= board[i][3-i];

		rowState = board[i][0];
		colState = board[0][i];

		for(int k=0; k < 4; k++)
		{
			rowState &= board[i][k];
			colState &= board[k][i];
		}

		if(rowState > 0)
		{
			return rowState;
		}
		else if(colState > 0)
		{
			return colState;
		}
	}

	if(diagonalState > 0)
	{
		return diagonalState;
	}
	else if(secondDiagonalState > 0)
	{
		return secondDiagonalState;
	}

	return 0;
}