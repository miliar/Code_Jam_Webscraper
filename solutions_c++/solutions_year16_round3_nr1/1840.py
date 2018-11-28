#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <string>

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

		std::vector<std::pair<int, char>> senators(n);
		for (int i = 0; i < n; i++)
		{
			int count;
			in >> count;

			senators[i] = { count, 'A' + i };
		}

		std::vector<std::string> plan;

		while (senators.size())
		{
			std::sort(senators.rbegin(), senators.rend());

			std::string step;
			if (senators[0].first == 1 && senators.size() % 2)
			{
				step += senators[0].second;
				senators[0].first--;
			}
			else if (senators[0].first == senators[1].first)
			{
				step += senators[0].second;
				step += senators[1].second;
				senators[0].first--;
				senators[1].first--;
			}
			else
			{
				step += senators[0].second;
				step += senators[0].second;
				senators[0].first -= 2;
			}

			plan.push_back(step);

			if (senators[0].first == 0)
				senators.erase(senators.begin());

			if (senators[0].first == 0)
				senators.erase(senators.begin());
		}

		out << "Case #" << t << ": ";
		std::copy(plan.begin(), plan.end(), std::ostream_iterator<std::string>(out, " "));
		out << std::endl;
	}

	return 0;
}