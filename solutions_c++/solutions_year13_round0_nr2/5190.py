#include <iostream>
#include <fstream>
#include <vector>
#include <map>

void print_output(int index, bool status);

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		std::cout << "Usage: Lawnmower.exe <input_file>" << std::endl;
		return -1;
	}

	std::ifstream input(argv[1], std::ios::in);
	int index_limit = -1;
	input >> index_limit;

	for (int index = 1; index <= index_limit; ++index)
	{
		int x_size = -1;
		input >> x_size;
		int y_size = -1;
		input >> y_size;

		std::vector<std::vector<std::pair<int, std::pair<bool, bool> > > >field(x_size);
		int buffer;
		for (int i = 0; i < x_size; ++i)
		{
			for (int j = 0; j < y_size; ++j)
			{
				input >> buffer;
				field[i].push_back(std::make_pair<int, std::pair<bool, bool> >(buffer, std::make_pair<bool, bool>(true, true)));
			}
		}

		bool valid = true;
		for (int i = 0; i < x_size && valid; ++i)
		{
			for (int j = 0; j < y_size && valid; ++j)
			{
				bool row_valid = true;
				// Check row
				for (int k = j + 1; k < y_size && valid; ++k)
				{
					if (field[i][j].first < field[i][k].first)
					{
						row_valid = false;
					}
					if (field[i][j].first > field[i][k].first)
					{
						field[i][k].second.first = false;
					}
				}

				bool col_valid = true;
				// Check col
				for (int k = i + 1; k < x_size && valid; ++k)
				{
					if (field[i][j].first < field[k][j].first)
					{
						col_valid = false;
					}
					if (field[i][j].first > field[k][j].first)
					{
						field[k][j].second.second = false;
					}
				}

				valid = (field[i][j].second.first && row_valid) || (field[i][j].second.second && col_valid);
			}
		}

		print_output(index, valid);
	}

	return 0;
}

void print_output(int index, bool status)
{
	std::cout << "Case #" << index << ": ";
	switch(status)
	{
		case true:
			std::cout << "YES";
			break;
		case false:
			std::cout << "NO";
			break;
		default:
			std::cout << "### Wrong status ###";
	}
	std::cout << std::endl;
}

