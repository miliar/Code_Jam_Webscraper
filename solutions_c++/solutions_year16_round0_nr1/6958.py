#include <fstream>
#include <unordered_set>

int main()
{
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		long long n;
		in >> n;

		if (n != 0)
		{
			int i;
			std::unordered_set<int> digits;
			for (i = 1; digits.size() < 10; i++)
			{
				long long current = i * n;
				while (current)
				{
					digits.insert(current % 10);
					current /= 10;
				}
			}

			out << "Case #" << t << ": " << (i - 1) * n << std::endl;
		}
		else
		{
			out << "Case #" << t << ": INSOMNIA" << std::endl;
		}
	}

	return 0;
}