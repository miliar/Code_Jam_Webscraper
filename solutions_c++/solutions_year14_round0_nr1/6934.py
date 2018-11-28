#include <iostream>

int main(void)
{
	int nbTests;
	std::cin >> nbTests;
	int firstAnswer, secondAnswer;
	int firstCards[4][4], secondCards[4][4];
	for(int t = 1; t <= nbTests; ++t)
	{
		std::cin >> firstAnswer;
		--firstAnswer;
		for(int y = 0; y < 4; ++y)
			for(int x = 0; x < 4; ++x)
				std::cin >> firstCards[x][y];
		std::cin >> secondAnswer;
		--secondAnswer;
		for(int y = 0; y < 4; ++y)
			for(int x = 0; x < 4; ++x)
				std::cin >> secondCards[x][y];
		int card = 0;
		bool multiple = false;
		for(int f = 0; f < 4; ++f)
			for(int s = 0; s < 4; ++s)
				if(firstCards[f][firstAnswer] == secondCards[s][secondAnswer])
				{
					if(card)
					{
						f = s = 4;
						multiple = true;
					}
					else
						card = secondCards[s][secondAnswer];
				}
		if(multiple)
			std::cout << "Case #" << t << ": Bad magician!\n";
		else if(card)
			std::cout << "Case #" << t << ": " << card << "\n";
		else
			std::cout << "Case #" << t << ": Volunteer cheated!\n";
	}
	return 0;
}
