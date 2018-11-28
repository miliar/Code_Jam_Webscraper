#include <iostream>
#include <fstream>
#include <string>
#include <map>

int main(char * argv[], int argc)
{
	std::ifstream file_input("data.in", std::ifstream::in);
	std::ofstream file_output("data.out", std::ofstream::out);
	int n_tests = 0;
	file_input >> n_tests;
	for (int iter1 = 0; iter1 < n_tests; iter1 += 1)
	{
		std::map<int, int> shyness_map;
		std::string input_string;
		int max_shy = 0;
		file_input >> max_shy;
		file_input >> input_string;
		for (int iter2 = 0; iter2 <= max_shy; iter2 += 1)
		{
			shyness_map[iter2] = std::stoi(input_string.substr(iter2, 1));
		}
		int n_standing = 0;
		int n_friends = 0;
		std::map<int, int>::iterator it;
		if (iter1 == 6)
		{
			int sdfgsd = 453;
		}
		for (it = shyness_map.begin(); it != shyness_map.end(); it++)
		{
			if (n_standing >= it->first)
			{
				n_standing += it->second;
			}
			else
			if ( it->second != 0)
			{ 
				n_friends += it->first - n_standing;
				n_standing += n_friends;
				n_standing += it->second;
			}
		}
		file_output << "Case #" << (iter1 + 1) << ": " << n_friends << std::endl;
	}
}