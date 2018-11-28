#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <iomanip>

int main()
{
	std::ifstream file("B-large.in");
	std::ofstream out("bout.txt");

	int tests;

	file >> tests;
	std::cout << tests << std::endl;

	for (int i = 0; i < tests; ++i)
	{
		long double rate = 2;
		long double farm_price;
		file >> farm_price;

		long double farm_bonus;
		file >> farm_bonus;

		long double goal;
		file >> goal;

		long double best = goal / rate;
		long double farm_time = 0;
		long double new_best = best;
		do
		{
			best = new_best;
			 farm_time += farm_price / rate;
			rate += farm_bonus;
			new_best = (goal / rate) + farm_time;
		}
		while (new_best < best);

        out << "Case #" << i+1 << ": " << std::fixed << std::setprecision(7) << best << std::endl;
		}
}