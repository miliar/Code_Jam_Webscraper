#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <map>

int costofNumber(const std::vector<int>& v, int diviseur);
int how_much(int k, int l);

int main()
{
	std::ifstream file("B-large.in");
	std::ofstream file2("answer.txt");
	int number_test_case = 0;

	file >> number_test_case;


	for (int i = 0; i < number_test_case; ++i)
	{
		int number_eaters = 0;

		file >> number_eaters;
		std::vector<int> test(number_eaters);

		for (int j = 0; j < number_eaters; ++j)
		{
			int c;
			file >> c;

			test[j] = c;
		}

		int end = *std::max_element(std::begin(test),std::end(test));
		int min = end;
		int diviseur = 0;

		for (int k = 1; k < end; ++k)
		{
			int r = costofNumber(test, k);
			if (r + k < min) min = r + k;
		}

		file2 << "Case #" << i+1 << ": " << min << std::endl;
	}
}

int costofNumber(const std::vector<int>& v, int diviseur)
{
	int res = 0;

	for (const auto& e : v)
	{
		if (e > diviseur)
			res += how_much(e, diviseur);
	}
	
	return res;
}

int how_much(int k, int l)
{
	return (std::ceil(float(k) / (float)l) - 1 );
}