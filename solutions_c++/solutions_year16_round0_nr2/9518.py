// revenge of the pancakes soln in cpp for google code jam by steven a dunn

#include <cstdio>
#include <fstream>
#include <string>

using std::ifstream;
using std::string;

int main (int argc, char* const argv[])
{
	ifstream input_file(argv[1]);
	if (input_file)
	{
		string line;

		// throw away first line
		getline(input_file, line);

		int line_count = 1;
		while (getline(input_file, line))
		{
			int flip_count = 0;
			char cur = line[0];
			for (int i = 1; i < line.size()-1; ++i)
			{
				if (cur != line[i])
				{
					cur = line[i];
					++flip_count;
				}
			}
			// special case the end for simplicity
			int last = line[line.size()-1];
			if (cur == '-')
				++flip_count;
			else
			{
				if (last == '-')
					flip_count += 2;
			}
			printf("Case #%d: %d \n", line_count, flip_count);
			++line_count;
		} 
		input_file.close();
	}
	return 0;
}