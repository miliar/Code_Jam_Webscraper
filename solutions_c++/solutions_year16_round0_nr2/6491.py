#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

unsigned int pancake(const string& stack) 
{
	size_t length = stack.size();
	vector<unsigned int> all_one(length), all_zero(length);
	
	all_one[0] = (stack[0] == '+') ? 0 : 1;
	all_zero[0] = (stack[0] == '-') ? 0 : 1;
	for (unsigned i = 1; i < length; i++)
	{
		if (stack[i - 1] == '-' && stack[i] == '-')
		{
			all_one[i] = all_one[i - 1];
			all_zero[i] = all_zero[i - 1];
		}
		else if (stack[i - 1] == '-' && stack[i] == '+')
		{
			all_one[i] = all_one[i - 1];
			all_zero[i] = min(all_one[i - 1] + 1, all_zero[i - 1] + 2); //**
		}
		else if (stack[i - 1] == '+' && stack[i] == '-')
		{
			all_one[i] = min(all_zero[i - 1] + 1, all_one[i - 1] + 2); //**
			all_zero[i] = all_zero[i - 1];
		}
		else if (stack[i - 1] == '+' && stack[i] == '+')
		{
			all_one[i] = all_one[i - 1];
			all_zero[i] = all_zero[i - 1];
		}
	}
	return all_one.back();
}

int main(int argc, char *argv[])
{
    std::ifstream file("B-large.in");
	std::ofstream ofile("output.txt");
    std::string str;
	std::getline(file, str);
	int i = 1;
    while (std::getline(file, str))
    {
		ofile << "Case #" << i++ << ": " << pancake(str) << endl;
    }
	return 0;
}