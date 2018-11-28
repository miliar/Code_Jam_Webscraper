#include <iostream>

int main()
{
	int T;
	std::cin >> T;
	int ans1, ans2;
	int num1[4][4];
	int num2[4][4];
	int number;
	int count = 0;
	for(int round = 1; round <= T; ++round)
	{
		std::cin >> ans1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			{
				std::cin >> num1[i][j];
			}

		std::cin >> ans2;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			{
				std::cin >> num2[i][j];
			}

		count = 0;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			{
				if(num1[ans1 - 1][i] == num2[ans2 - 1][j])
				{
					count++;
					number = num1[ans1 - 1][i];
				}
			}

		if(count == 0)
		{
			std::cout << "Case #" << round << ": Volunteer cheated!" << std::endl;
		}
		else if(count == 1)
		{
			std::cout << "Case #" << round << ": " << number << std::endl;
		}
		else
		{
			std::cout << "Case #" << round << ": Bad magician!" << std::endl;
		}
	}
}
