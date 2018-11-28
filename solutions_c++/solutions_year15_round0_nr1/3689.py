#include <fstream>
#include <string>
#include <vector>

int main()
{
	std::ifstream file("A-large.in");
	std::ofstream file2("answer.txt");
	int number_test_case = 0;

	file >> number_test_case;

	for (int i = 0; i < number_test_case; ++i)
	{
		int smax = 0;

		file >> smax;
		std::vector<int> test(smax+1);

		for (int j = 0; j < smax + 1; ++j)
		{
			char c;
			file >> c;

			test[j] = c - '0';
		}

		int actual_sum = 0;
		int need = 0;
		int res = 0;

		for (auto& e : test)
		{
			if (actual_sum + res < need)
				res += need - (actual_sum + res);

			actual_sum += e;
			++need;
		}

		file2 << "Case #" << i+1 << ": " << res << std::endl;
	}
}