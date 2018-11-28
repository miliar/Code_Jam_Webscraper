// counting sheep soln for google code jam 2016 by steven a dunn

#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using std::ifstream;
using std::ostringstream;
using std::string;
using std::vector;

string make_string(long);
int count_digits(string, vector<int>&);

int main (int argc, char* const argv[])
{
	ifstream input_file(argv[1]);
	if (input_file)
	{
		string line;
		getline(input_file, line);

		int line_count = 1;
		while (getline(input_file, line))
		{
			long N = atol(line.c_str());
			if (N == 0)
			{
				printf("Case #%d: INSOMNIA \n", line_count);
				++line_count;
				continue;
			}

			vector<int> found(10, 0);
			int idx = 2;
			long val = N;
			while (true)
			{
				string digits = make_string(val);
				int dig_count = count_digits(digits, found);
	
				if (dig_count == 10)
				{
					printf("Case #%d: %s \n", line_count, digits.c_str());
					break;
				}

				val = N * idx;
				++idx;
			}
			++line_count;
		}
		input_file.close();
	}
	return 0;
}

string make_string(long N)
{
	ostringstream converter;
	converter << N;
	return converter.str();
}

int count_digits(string digits, vector<int>& found)
{
	for (int i = 0; i < digits.size(); ++i)
	{
		found[digits[i]-'0'] = 1;
	}

	int dig_count = 0;
	for (int i = 0; i < 10; ++i)
		if (found[i] == 1)
			++dig_count;
	return dig_count;
}