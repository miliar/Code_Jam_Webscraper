#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <utility>



int main()
{
	std::ifstream file("C-small-attempt0.in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	int palyndromic_squares[] = {0, 1, 4, 9, 121, 484};

	int nb;
	file >> nb;

	for(int j = 0; j < nb; ++j)
	{
		long long interval_min, interval_max;
		file >> interval_min;
		file >> interval_max;

		int count = 0;

		for(auto c : palyndromic_squares)
		{
			if(c >= interval_min && c <= interval_max) count++;
		}
		
		file2 << "Case #" << j + 1 << ": " << count << std::endl;
	}
}