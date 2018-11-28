#include <iostream>
#include <fstream>
#include <string>

#define MAX_LINE_LENGTH 1024

using namespace std;

void print_usage(char *prog_name)
{
	cout << "Usage: " << prog_name << " <input_file>\n";
	return;
}

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		print_usage(argv[0]);
		return 0;
	}

	ifstream input_file;
	int file_index, line_count, line_index, test_count, test_index, blank_index;
	string line, line1, line2;
	char c_line[MAX_LINE_LENGTH];
	int sum_of_audience, total_needed_friends, needed_friends;

	for (file_index = 1; file_index < argc; file_index++)
	{
		input_file.open(argv[file_index], ios::in | ios::app);
		if (!input_file.is_open())
		{
			cout << "ERROR: cannot open input file: " << argv[file_index] << endl;
			continue;
		}

		//cout << argv[file_index] << endl;

		getline(input_file, line);
		line_count = stoi(line);
		
		//cout << "LINE COUNT = " << line_count << endl;
		for (line_index = 0; line_index < line_count; line_index++)
		{
			getline(input_file, line);
			// cout << line << "\t";
			blank_index = line.find_first_of(' ');
			// cout << blank_index << endl;
			line1 = line.substr(0, blank_index);

			blank_index = line.find_last_of(' ');
			// cout << blank_index << endl;
			line2 = line.substr(blank_index+1, line.length() - blank_index);

			//cout << line1 << "\t" << line2 << endl;

			test_count = stoi(line1);
			sum_of_audience = 0;
			total_needed_friends = 0;

			strcpy_s(c_line, MAX_LINE_LENGTH, line2.c_str());
			if (test_count == 0)
			{
				total_needed_friends = 0;
			}
			else if (test_count == 1)
			{
				char char_digit = c_line[0];
				if (char_digit == '0')
				{
					total_needed_friends = 1;
				}
				else
				{
					total_needed_friends = 0;
				}
			}
			else
			{
				for (test_index = 0; test_index < test_count; test_index++)
				{
					char char_digit = c_line[test_index];
					int int_digit = (int)(char_digit - '0');

					needed_friends = 0;

					if (test_index > 0)
					{
						if ((sum_of_audience + int_digit) <= test_index)
						{
							needed_friends = test_index - sum_of_audience;
							if (needed_friends == 0) 
							{
								needed_friends = 1;
							}
							total_needed_friends += needed_friends;
						}
					}
					//cout << (char)('0' + needed_friends);
					sum_of_audience += int_digit + needed_friends;
				}
				//cout << endl;
			}
			cout << "Case #" << line_index + 1 << ": " << total_needed_friends << endl; 
		}

		input_file.close();
	}

	return 0;
}