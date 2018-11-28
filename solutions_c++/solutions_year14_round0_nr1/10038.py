#include <iostream>
#include <set>

int main()
{
	int t;
	std::cin >> t;
	for (int i = 0; i < t; ++i)
	{
		std::set<int> x;
		for (int j = 0; j < 16; x.insert(++j));
		for (int j = 0; j < 2; ++j)
		{
			int r;
			std::cin >> r;
			for (int k = 1; k < 5; ++k)
			{
				for (int l = 0; l < 4; ++l)
				{
					int y;
					std::cin >> y;
					if (k != r)
					{
						x.erase(y);
					}
				}
			}
		}
		std::cout << "Case #" << i + 1 << ": ";
		if (x.size() == 1)
		{
			std::cout << *x.begin();
		}
		else if (x.size() > 1)
		{
			std::cout << "Bad magician!";
		}
		else
		{
			std::cout << "Volunteer cheated!";
		}
		std::cout << std::endl;
	}
}