#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>

char ctrl(std::string matrix)
{
	for (int x = 0; x < 16; x += 4)
	{
		char ref = matrix[x];
		if (ref == '.') continue;
		bool win = true;
		for (int y = x + 1; y < x + 4; y++)
		{
			if ( matrix[y] == '.' || (matrix[y] != ref && matrix[y] != 'T') )
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			return ref;
		}

	}
	for (int x = 0; x < 4; x++)
	{
		char ref = matrix[x];
		if (ref == '.') continue;
		bool win = true;
		for (int y = x + 4; y < 16; y += 4)
		{
			if ( matrix[y] == '.' || (matrix[y] != ref && matrix[y] != 'T') )
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			return ref;
		}

	}
	if (matrix[0] != '.')
	{
		char ref = matrix[0];
		bool win = true;
		for (int y = 5; y < 16; y += 5)
		{
			if ( matrix[y] == '.' || (matrix[y] != ref && matrix[y] != 'T') )
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			return ref;
		}
	}
	if (matrix[3] != '.')
	{
		char ref = matrix[3];
		bool win = true;
		for (int y = 6; y < 13; y += 3)
		{
			if ( matrix[y] == '.' || (matrix[y] != ref && matrix[y] != 'T') )
			{
				win = false;
				break;
			}
		}
		if (win)
		{
			return ref;
		}
	}

	return NULL;
}

int main(int argc, char **argv)
{
	std::ifstream input(argv[1]);

	int T;
	input >> T;

	char win;
	for (int i = 1; i <= T; i++)
	{
		std::string row, matrix;
		for (int x = 0; x < 4; x++)
		{
			input >> row;
			matrix = matrix + row;
		}
		if ( win = ctrl(matrix) )
		{
			std::cout << "Case #" << i << ": " << win << " won" << std::endl;
		}
		else if (matrix.find('.') != std::string::npos)
		{
			std::cout << "Case #" << i << ": Game has not completed" << std::endl;
		}
		else
		{
			std::cout << "Case #" << i << ": Draw" << std::endl;
		}
	}

	input.close();
}
