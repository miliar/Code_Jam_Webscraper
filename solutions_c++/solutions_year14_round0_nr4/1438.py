#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	int T;
	std::cin >> T;
	std::vector<double> naomi1;
	std::vector<double> ken1;
	std::vector<double> naomi2;
	std::vector<double> ken2;
	int y, z;
	int count;

	for(int round = 1; round <= T; ++round)
	{
		std::cin >> count;
		double weight;
		naomi1.clear();
		ken1.clear();
		naomi2.clear();
		ken2.clear();
		for(int i = 0; i < count; ++i)
		{
			std::cin >> weight;
			naomi1.push_back(weight);
			naomi2.push_back(weight);
		}
		for(int i = 0; i < count; ++i)
		{
			std::cin >> weight;
			ken1.push_back(weight);
			ken2.push_back(weight);
		}
		std::sort(naomi1.begin(), naomi1.end());
		std::sort(ken1.begin(), ken1.end());
		std::sort(naomi2.begin(), naomi2.end());
		std::sort(ken2.begin(), ken2.end());
		y = 0;
		for(int i = 0; i < count; ++i)
		{
			if(naomi1[0] < ken1[0])
			{
				naomi1.erase(naomi1.begin());
				ken1.pop_back();
			}
			else
			{
				naomi1.erase(naomi1.begin());
				ken1.erase(ken1.begin());
				y++;
			}
		}

		z = 0;
		for(int i = 0; i < count; ++i)
		{
			if(naomi2[0] > ken2[ken2.size() - 1])
			{
				z = naomi2.size();
				break;
			}
			else
			{
				for(int j = 0; j < ken2.size(); ++j)
				{
					if(ken2[j] < naomi2[0])
					{
						continue;
					}
					else
					{
						naomi2.erase(naomi2.begin());
						ken2.erase(ken2.begin() + j);
						break;
					}
				}
			}
		}

		std::cout << "Case #" << round << ": " << y << " " << z << std::endl;
	}

	return 0;
}
