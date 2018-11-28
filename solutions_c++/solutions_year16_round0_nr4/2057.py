#include <iostream>
#include <fstream>
#include <sstream>

#include <string>
#include <vector>
#include <cmath>

using namespace std;

void useage()
{
	cout << "The program accepts only one argument that is the name of the input file" << endl;
	cout << "Counting_Sheep <full_input_file_name>" << endl;
}

int main(int argc, char **argv)
{
	char* input_file_name;
	if (argc == 1)
	{
		cout << "Error: need one argument to specify the name of the input file" << endl;
		useage();
		return -1;
	}
	else if (argc >= 3)
	{
		cout << "Error: two many arguments" << endl;
		useage();
		return -1;
	}
	else
	{
		input_file_name = argv[1];
	}

	fstream in, out;
	in.open(input_file_name, fstream::in);
	if (!in.is_open())
	{
		cout << "Error: the input file is unable to be opened." << endl;
		return -2;
	}
	out.open("output.txt", fstream::out);
	if (!out.is_open())
	{
		cout << "Error: the output file (output.txt) is unable to be opened." << endl;
		return -2;
	}

	unsigned int total_test;
	unsigned long long k, c, s;
	string newline_char;
	in >> total_test;
	getline(in, newline_char); //remove the newline character
	for (unsigned int test_id = 1; test_id <= total_test; test_id++)
	{
		//parse each test case
		in >> k;
		in >> c;
		in >> s;
		getline(in, newline_char); //remove the newline character
		vector<unsigned long long> tiles_to_clean; //the indices of tiles to clean, the index is 1-based.

		//first, determine if possible; if possible, find the indices of tiles
		if (c == 1)
		{
			if (k <= s)
			{
				unsigned long long cur_idx = 1;
				while (cur_idx <= k)
				{
					tiles_to_clean.push_back(cur_idx);
					cur_idx++;
				}
			}
		}
		else 
		{
			if (k <= c || s >= (k / c + ((k % c == 0) ? 0 : 1)))
			{
				unsigned long long pre = 0, x = 1, y = c;
				while (x < k) 
				{
					if (y == 1)
					{
						tiles_to_clean.push_back(1+pre);
						y = c;
						pre = x;
					}
					else
					{
						pre = pre*k + x;
						y--;
					}
					x++;
				}
				//if y==1, then the last tile is 1+ pre; otherwise, it's 1 + pre*k^(y-1)
				tiles_to_clean.push_back(1 + pre * (unsigned long long) pow(1.0*k, 1.0*(y-1)));
			}
		}

		//output the result for the case
		out << "Case #" << test_id << ": ";
		if (tiles_to_clean.empty())
			out << "IMPOSSIBLE" << endl;
		else
		{
			//output each tile's index appended by a space except the last tile index
			for (unsigned int i = 0; i < tiles_to_clean.size() - 1; i++)
				out << tiles_to_clean[i] << " ";
			//output the last tile appended by a newline character
			out << tiles_to_clean.back() << endl;
		}
	}

	in.close();
	out.close();

	return 0;
}