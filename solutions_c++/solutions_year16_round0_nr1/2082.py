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
	unsigned int picked_num;
	unsigned int current_num;
	unsigned int find_all_digits = 0x3FF;
	in >> total_test;
	for (unsigned int test_id = 1; test_id <= total_test; test_id++)
	{
		//parse each test case
		in >> picked_num;
		current_num = 0;
		//process the test case
		if (picked_num != 0)
		{
			unsigned int digits_found_by_now = 0;
			unsigned int temp_num;
			bool appeared_digits[10] = { false };

			while (digits_found_by_now != find_all_digits) // the while loop will run at most 45 iterations
			{
				//each step: N*k -> N*(k+1)
				current_num += picked_num;
				temp_num = current_num;
				unsigned int last_digit_in_num;
				while (temp_num != 0)
				{
					last_digit_in_num = temp_num % 10;
					if (appeared_digits[last_digit_in_num] == false)
					{
						appeared_digits[last_digit_in_num] = true;
						digits_found_by_now |= (1 << last_digit_in_num);
					}
					temp_num /= 10;
				}
			}
		}
		//output the result for the case
		out << "Case #" << test_id << ": ";
		if (current_num == 0)
		{
			out << "INSOMNIA";
		}
		else
			out << current_num;
		out << endl;
	}

	in.close();
	out.close();

	return 0;
}