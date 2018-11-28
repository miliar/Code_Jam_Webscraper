#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <string>

int main()
{
	std::ifstream input("input.txt");
	std::ofstream output("output.txt");

	if (!input.is_open())
		return printf("Failed to open file\n");

	int cases = 0;

	std::string line;
	getline(input, line);

	cases = atoi(line.c_str());

	for (int i = 0; i < cases; ++i)
	{
		int answer[2];
		int cards[2][4][4];

		getline(input, line);
		answer[0] = atoi(line.c_str());

		for (int row = 0; row < 4; ++row)
		{
			getline(input, line);
			sscanf(line.c_str(), "%d %d %d %d", &cards[0][row][0], &cards[0][row][1], &cards[0][row][2], &cards[0][row][3]);
		}

		getline(input, line);
		answer[1] = atoi(line.c_str());

		for (int row = 0; row < 4; ++row)
		{
			getline(input, line);
			sscanf(line.c_str(), "%d %d %d %d", &cards[1][row][0], &cards[1][row][1], &cards[1][row][2], &cards[1][row][3]);
		}

		int result = 0;

		for (int x = 0; x < 4; ++x)
		{
			for (int y = 0; y < 4; ++y)
			{
				if (cards[0][answer[0]-1][x] == cards[1][answer[1]-1][y])
				{
					if (result != 0)
					{
						result = -1;   /* Bad magic*/
						break;
					}
					result = cards[0][answer[0]-1][x];
				}

				if (result == -1)
					break;

			}
		}

		char keks[256] = {0};
		switch (result)
		{
			case -1:
				sprintf(keks, "Case #%d: Bad magician!\n", i+1);
				output.write(keks, strlen(keks));
				printf("Case #%d: Bad magician!\n", i+1);
				break;
			case 0:
				sprintf(keks, "Case #%d: Volunteer cheated!\n", i+1);
				printf("Case #%d: Volunteer cheated!\n", i+1);
				output.write(keks, strlen(keks));
				break;
			default:
				sprintf(keks, "Case #%d: %d\n", i+1, result);
				printf("Case #%d: %d\n", i+1, result);
				output.write(keks, strlen(keks));
				break;
		}

		output.flush();
	}

	output.close();

	std::cin >> line;

	return 0;
}