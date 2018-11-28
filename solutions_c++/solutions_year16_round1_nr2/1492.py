#include <vector>
#include <fstream>
#include <iterator>

int main()
{
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		int n;
		in >> n;

		std::vector<int> occurances(2501);
		for (int i = 0; i < 2 * n - 1; i++)
		{
			std::vector<int> list(n);
			std::copy_n(std::istream_iterator<int>(in), n, list.begin());

			for (int v : list)
				occurances[v]++;
		}

		std::vector<int> missing;
		for (int i = 0; i <= 2500; i++)
		{
			if (occurances[i] % 2 == 1)
				missing.push_back(i);
		}

		out << "Case #" << t << ": ";
		std::copy(missing.begin(), missing.end(), std::ostream_iterator<int>(out, " "));
		out << std::endl;
	}
}