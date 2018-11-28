/*
	a.cpp
	Christopher Cabrera
	Magic Trick - Code Jam 2014 Qualification
*/

#include <iomanip>
#include <iostream>
#include <vector>

int main()
{
	int ans, num_ans, T, told_row, card;
	std::vector<int> card_row;

	std::cin >> T;

	for (int t = 0; t < T; ++t)
	{
		card_row.clear();
		ans = 0; num_ans = 0;

		std::cin >> told_row;
		for (int r = 0; r < 4; ++r)
		{
			for (int c = 0; c < 4; ++c)
			{
				if (told_row == (r + 1))
				{
					std::cin >> card;
					card_row.push_back(card);
				}
				else
					std::cin >> card;
			}
		}

		std::cin >> told_row;
		for (int r = 0; r < 4; ++r)
		{
			for (int c = 0; c < 4; ++c)
			{
				if (told_row == (r + 1))
				{
					std::cin >> card;
					for (int i = 0; i < 4; ++i)
					{
						if (card == card_row[i])
						{
							ans = card;
							++num_ans;
						}
					}
				}
				else
					std::cin >> card;
			}
		}

		// print answer
		std::cout << "Case #" << t + 1 << ": ";
		if (num_ans == 1)
			std::cout << ans << '\n';
		else if (num_ans == 0)
			std::cout << "Volunteer cheated!\n";
		else	// num_ans > 1
			std::cout << "Bad magician!\n";	
	}

	return 0;
}