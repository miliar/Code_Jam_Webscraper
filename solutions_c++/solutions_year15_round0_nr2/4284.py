#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main(char * argv[], int argc)
{
	std::ifstream file_input("data.in", std::ifstream::in);
	std::ofstream file_output("data.out", std::ofstream::out);
	int n_tests = 0;
	file_input >> n_tests;
	for (int iter1 = 0; iter1 < n_tests; iter1 += 1)
	{
		std::vector<int> diner_vec;
		int known_minimum = 0;
		int n_diners = 0;
		file_input >> n_diners;
		for (int iter2 = 0; iter2 < n_diners; iter2 += 1)
		{
			int value = 0;
			file_input >> value;
			diner_vec.push_back(value);
			if (value > known_minimum)
			{
				known_minimum = value;
			}
		}
		int n_cycles = 2;
		std::vector<int>::iterator it;
		
		while (n_cycles < known_minimum)
		{
			int total = 0;
			for (it = diner_vec.begin(); it != diner_vec.end(); it++)
			{
				total += ((*it - 1) / n_cycles);
			}
			total += n_cycles;
			if (total < known_minimum)
			{
				known_minimum = total;
			}
			n_cycles++;
		}
		file_output << "Case #" << (iter1 + 1) << ": " << known_minimum << std::endl;
	}
}