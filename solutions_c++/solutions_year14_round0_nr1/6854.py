#include <iostream>

void DoTest()
{
	int first_answer, second_answer;
	std::cin >> first_answer;
	int possible[4];
	int new_row[4];
	for (int i = 1; i <= 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int tmp;
			std::cin >> tmp;
			if (i == first_answer)
				possible[j] = tmp;
		}
	}

	std::cin >> second_answer;
	for (int i = 1; i <= 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int tmp;
			std::cin >> tmp;
			if (i == second_answer)
				new_row[j] = tmp;
		}
	}

	int the_same = 0;
	int same = -1;


	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (possible[i] == new_row[j])
			{
				the_same++;
				same = possible[i];
				break;
			}
		}
	}

	if (the_same == 1)
		std::cout << same << '\n';
	else if (the_same == 0)
		std::cout << "Volunteer cheated!\n";
	else
		std::cout << "Bad magician!\n";
}

int main()
{
	//std::ios::sync_with_stdio(0);
	//std::cin.tie(NULL);
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; i++)
	{
		std::cout << "Case #" << i << ": ";	
		DoTest();
	}
}
