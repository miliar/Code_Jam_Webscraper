#include "proba.h"
#include <fstream>
#include <iostream>
#include <string>
#include "math.h"


using namespace std;

int main(int argc, char const *argv[])
{
	string line;
	string inFile = "A-large.in"; // open the file and obtain an open stream
	string oFile_name = "A-large_out.txt";
	int main_count = 0;
	
	ofstream ofs;
	ofs.open(oFile_name);

	ifstream ist(inFile);
	if (!ist) return -1;

	// first line contains the number of cases
	getline(ist, line);
	int num_cases = stoi(line);
	int result{};

	while (getline(ist,line))
	{
		++main_count;
		result = count_sheep(stoi(line));

		if (result == -1)
		{
			ofs << "Case #" << main_count << ": " << "INSOMNIA" << endl;
		}
		else
		{
			ofs << "Case #" << main_count << ": " << result << endl;
		}
	}

	return 0;
}

int count_sheep(int num_in)
{
	// if (only5s(num_in)) return -1;
	if (num_in == 0) return -1;
	
	int num_digits = get_num_digits(num_in);
	int base10digits[10]{};
	int count{0};

	vector<int> digits = separate_digits(num_in, num_digits);

	for (auto y : digits)
	{
		if (base10digits[y] == 0)
		{
			base10digits[y]= 1;
		}
	}

	for (auto y : base10digits)
	{
		if (y == 1) count++;
	}

	if (count == 10) return num_in;

	int do_counter{1};
	int do_num_in = num_in;
	vector<int> do_digits;
	do
	{
		++do_counter;
		count = 0; //reset the counter

		do_num_in = do_counter * num_in;
		do_digits = separate_digits(do_num_in, get_num_digits(do_num_in));

		for (auto y : do_digits)
		{
			if (base10digits[y] == 0)
			{
				base10digits[y] = 1;
			}
		}

		for (auto y : base10digits)
		{
			if (y == 1) count++;
		}
	}while(count != 10);

	return (do_counter * num_in);
}

bool only5s (int num_in)
{
	// check that prime factorization of the number only contains 5's
	if (num_in % 10 == 5 || num_in % 10 == 0)
	{
		do
		{
			if (num_in == 1) return true;

			if (num_in % 5 == 0)
			{
				num_in /= 5;
			}
			else
			{
				return false;
			}
		}while(num_in > 0);
		return true;
	}
	return false;
}

vector<int> separate_digits(int value, int num_digits)
{
	vector<int> digits;

	int digit{};

	for (int i = num_digits - 1; i > -1; --i)
	{
		digit = int(value / pow(10,i)) % 10;
		digits.push_back(digit);
	}
	return digits;
}

int get_num_digits(int num_in)
{
	return (log10(num_in) + 1);
}