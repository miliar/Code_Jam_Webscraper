#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <utility>

int main()
{
	std::ifstream file("B-large (1).in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	int nb;
	file >> nb;

	for(int j = 0; j < nb; ++j)
	{
		int line, column;
		file >> line;
		file >> column;

		std::vector<int> lawn(line * column);
		std::vector<int> max_line(line), max_column(column);

		for(int i = 0; i < line*column; ++i)
		{
			file >> lawn[i];
		}

		// max of lines

		for(int i = 0; i < line; ++i)
		{
			max_line[i] = *std::max_element(lawn.begin() + i * column, lawn.begin() + (i+1) * column);
		}

		// max of columns

		for(int i= 0; i < column; ++i)
		{
			int max = 0;
			for(int k =0; k < line; ++k)
			{
				if(lawn[column * k + i] > max) max = lawn[column * k + i];
			}
			max_column[i] = max;
		}

		bool doable = true;
		for(unsigned int i = 0; i < line; ++i)
		{
			for(unsigned int k = 0; k < column; ++k)
			{
				int index = i*column + k;
				if(lawn[index] < max_line[i] && lawn[index] < max_column[k]) 
				{
					doable = false;
					break;
				}
			}
			if(!doable) break;
		}

		file2 << "Case #" << j + 1 << ": " << (doable ? "YES" : "NO") << std::endl;
	}
}