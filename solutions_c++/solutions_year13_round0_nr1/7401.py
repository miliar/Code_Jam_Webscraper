#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iterator>

void print2DVector(std::vector<std::vector<char>> in)
{
	for ( unsigned int i = 0; i < in.size(); i++ )
	{
		std::cout << i << ": ";
		for ( unsigned int j = 0; j < in[i].size(); j++ )
		{
			std::cout << in[i][j] << ", ";
		}
		std::cout << std::endl;
	}
}
void print1DVector(std::vector<int> in)
{
	for ( unsigned int i = 0; i < in.size(); i++ )
	{
		std::cout << in.at(i) << ", ";
	}
	std::cout << std::endl;
}
int checkRow(std::vector<char> row)
{
	if ( (row[0] == '.') || (row[1] == '.') || (row[2] == '.') || (row[3] == '.'))
	{
		return 3;
	}
	if ( ((row[0] == 'X') || (row[0] == 'T')) && ((row[1] == 'X') || (row[1] == 'T')) && ((row[2] == 'X') || (row[2] == 'T')) && ((row[3] == 'X') || (row[3] == 'T')) )
	{
		return 0;
	}
	else if ( ((row[0] == 'O') || (row[0] == 'T')) && ((row[1] == 'O') || (row[1] == 'T')) && ((row[2] == 'O') || (row[2] == 'T')) && ((row[3] == 'O') || (row[3] == 'T')) )
	{
		return 1;
	}
	else
	{
		return 2;
	}
}
std::vector<int> analyzeBoard(std::vector< std::vector<char> > board)
{
	std::vector< int > results;
	for ( int j = 0; j < 4; j++)
	{
		std::vector<char> row(board[j].begin(), board[j].end());
		results.push_back(checkRow(row));
	}
	for ( int j = 0; j < 4; j++)
	{
		char column[] = {board[0][j], board[1][j], board[2][j], board[3][j]};
		std::vector<char> row(std::begin(column), std::end(column));
		results.push_back(checkRow(row));
	}
	for ( int j = 0; j < 2; j++)
	{
		if ( j == 0 )
		{
			char column[] = {board[0][0], board[1][1], board[2][2], board[3][3]};
			std::vector<char> row(std::begin(column), std::end(column));
			results.push_back(checkRow(row));
		}
		else
		{
			char column[] = {board[3][0], board[2][1], board[1][2], board[0][3]};
			std::vector<char> row(std::begin(column), std::end(column));
			results.push_back(checkRow(row));
		}
	}
	return results;
}

int main()
{
	int n;
	std::string line;
	std::ifstream input ("file.in");
	std::ofstream output ("file.out");
	std::getline(input, line);
	std::istringstream(line) >> n;
	std::vector< std::vector<char> > board;
	std::vector< int > results;
	bool draw;
	bool complete;
	int victor;
	
	for ( int i = 0; i < n; i++)
	{
		for ( int j = 0; j < 4; j++)
		{
			std::getline(input, line);
			std::vector<char> row( line.begin(), line.end() );
			board.push_back(row);
		}
		std::getline(input, line);
		results = analyzeBoard(board);
		
		draw = 1;
		complete = 1;
		victor = 0;
		for ( unsigned int j = 0; j < results.size(); j++)
		{
			if (results[j] == 0)
			{
				victor = 1;
				draw = 0;
				
			}
			else if (results[j] == 1)
			{
				victor = 2;
				draw = 0;
			}
			else if (results[j] == 3)
			{
				complete = 0;
			}
		}
		if ( victor == 1 )
		{
			output << "Case #" << i+1 << ": X won" << std::endl;
		}
		else if ( victor == 2)
		{
			output << "Case #" << i+1 << ": O won" << std::endl;
		}
		else if ( complete == 0 )
		{
			output << "Case #" << i+1 << ": Game has not completed" << std::endl;
		}
		else if ( draw == 1 )
		{
			output << "Case #" << i+1 << ": Draw" << std::endl;
		}
		
		results.clear();
		board.clear();
	}
	
	return 0;
}
