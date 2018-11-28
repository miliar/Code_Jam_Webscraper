#include <iostream>
#include <fstream>
#include <sstream>

#include <string>
#include <vector>

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
	string initial_pancakes;
	unsigned int min_operatation;
	in >> total_test;
	getline(in, initial_pancakes); //remove the newline character
	for (unsigned int test_id = 1; test_id <= total_test; test_id++)
	{
		//parse each test case
		getline(in,initial_pancakes);
		min_operatation = 0;

		//process the test case
		int num_pancakes = initial_pancakes.size();
		char cur_side = '+';
		for (int cur_pancake_idx = num_pancakes - 1; cur_pancake_idx >= 0; cur_pancake_idx--)
		{
			if (cur_side != initial_pancakes[cur_pancake_idx])
			{
				cur_side = initial_pancakes[cur_pancake_idx];
				min_operatation++;
			}
		}
		//output the result for the case
		out << "Case #" << test_id << ": " << min_operatation << endl;
	}

	in.close();
	out.close();

	return 0;
}