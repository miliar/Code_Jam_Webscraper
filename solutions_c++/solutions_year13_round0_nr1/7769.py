#include <iostream>

#include <fstream>

//using namespace std;

enum SquareState {Empty, X, O, T};

void ReadInput(std::ifstream& inputFile, SquareState board[][4])
{
	char tmp;

	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			inputFile >> tmp;
			switch(tmp)
			{
			case 'X':
				board[i][j] = X;
				break;

			case 'O':
				board[i][j] = O;
				break;

			case 'T':
				board[i][j] = T;
				break;

			case '.':
				board[i][j] = Empty;
				break;
			}
		}
	}
}

bool searchLine(SquareState board[][4], SquareState& winner)
{
	bool isLine=true;
	std::size_t i=0;
	do
	{
		bool lineFull=true;
		for(std::size_t j=0; j<4; j++)
		{
			if(board[i][j] == Empty)
			{
				j=4;
				lineFull=false;
			}
		}
		if(lineFull)
		{
			isLine=true;
			std::size_t j=1;
			if(board[i][0]==T)
				j++;

			while(j<3)
			{
				if(board[i][j]!=board[i][j-1])
				{
					if(board[i][j]==T)
					{
						if(board[i][j+1]!=board[i][j-1])
							isLine=false;
						j++;
					}
					else
						isLine=false;
				}
				j++;
			}
			if(j==3)
			{
				if(board[i][j]!=board[i][j-1] && board[i][j]!=T)
					isLine=false;
			}
			if(isLine)
			{
				if(board[i][0] != T)
					winner = board[i][0];
				else
					winner = board[i][1];

				return true;
			}
		}

		i++;
	}while(i<4);

	return false;
}

bool searchColumn(SquareState board[][4], SquareState& winner)
{
	bool isColumn=true;
	std::size_t i=0;
	do
	{
		bool columnFull=true;
		for(std::size_t j=0; j<4; j++)
		{
			if(board[j][i] == Empty)
			{
				j=4;
				columnFull=false;
			}
		}
		if(columnFull)
		{
			isColumn=true;
			std::size_t j=1;
			if(board[0][i]==T)
				j++;

			while(j<3)
			{
				if(board[j][i]!=board[j-1][i])
				{
					if(board[j][i]==T)
					{
						if(board[j+1][i]!=board[j-1][i])
							isColumn=false;
						j++;
					}
					else
						isColumn=false;
				}
				j++;
			}
			if(j==3)
			{
				if(board[j][i]!=board[j-1][i] && board[j][i]!=T)
					isColumn=false;
			}
			if(isColumn)
			{
				if(board[0][i] != T)
					winner = board[0][i];
				else
					winner = board[1][i];

				return true;
			}
		}

		i++;
	}while(i<4);

	return false;
}

bool searchDiagonal(SquareState board[][4], SquareState& winner)
{
	bool diagonalFull=true;
	for(std::size_t j=0; j<4; j++)
	{
		if(board[j][j] == Empty)
		{
			j=4;
			diagonalFull=false;
		}
	}
	if(diagonalFull)
	{
		bool isDiagonal=true;
		isDiagonal=true;
		std::size_t j=1;
		if(board[0][0]==T)
			j++;

		while(j<3)
		{
			if(board[j][j]!=board[j-1][j-1])
			{
				if(board[j][j]==T)
				{
					if(board[j+1][j+1]!=board[j-1][j-1])
						isDiagonal=false;
					j++;
				}
				else
					isDiagonal=false;
			}
			j++;
		}
		if(j==3)
		{
			if(board[j][j]!=board[j-1][j-1] && board[j][j]!=T)
				isDiagonal=false;
		}
		if(isDiagonal)
		{
			if(board[0][0] != T)
				winner = board[0][0];
			else
				winner = board[1][1];

			return true;
		}
	}

	return false;
}

bool searchDiagonal2(SquareState board[][4], SquareState& winner)
{
	bool diagonalFull=true;
	for(std::size_t j=0; j<4; j++)
	{
		if(board[j][3-j] == Empty)
		{
			j=4;
			diagonalFull=false;
		}
	}
	if(diagonalFull)
	{
		bool isDiagonal=true;
		isDiagonal=true;
		std::size_t j=1;
		if(board[0][3]==T)
			j++;

		while(j<3)
		{
			if(board[j][3-j]!=board[j-1][4-j])
			{
				if(board[j][3-j]==T)
				{
					if(board[j+1][2-j]!=board[j-1][4-j])
						isDiagonal=false;
					j++;
				}
				else
					isDiagonal=false;
			}
			j++;
		}
		if(j==3)
		{
			if(board[j][3-j]!=board[j-1][4-j] && board[j][3-j]!=T)
				isDiagonal=false;
		}
		if(isDiagonal)
		{
			if(board[0][3] != T)
				winner = board[0][3];
			else
				winner = board[1][2];

			return true;
		}
	}

	return false;
}

bool isFull(SquareState board[][4])
{
	for(std::size_t i=0; i<4; i++)
	{
		for(std::size_t j=0; j<4; j++)
		{
			if(board[i][j] == Empty)
				return false;
		}
	}
	return true;
}

int main()
{
    SquareState board[4][4];
    std::ifstream input("A-large.in");
    int casesDracula=0;
	input >> casesDracula;

	std::ofstream output("output.txt");
	for(int i=0; i<casesDracula; i++)
	{
		ReadInput(input, board);
		input.ignore();
		SquareState winner=Empty;

		output << "Case #" << i+1 << ": ";
		if(searchLine(board, winner))
		{
			if(winner == X)
				output << "X won";
			else
				output << "O won";
		}
		else if(searchColumn(board, winner))
		{
			if(winner == X)
				output << "X won";
			else
				output << "O won";
		}
		else if(searchDiagonal(board, winner))
		{
			if(winner == X)
				output << "X won";
			else
				output << "O won";
		}
		else if(searchDiagonal2(board, winner))
		{
			if(winner == X)
				output << "X won";
			else
				output << "O won";
		}
		else if(isFull(board))
			 output << "Draw";
		else
			output << "Game has not completed";

		output << "\n";
	}

    return 0;
}
