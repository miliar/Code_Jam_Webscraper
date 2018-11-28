#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	std::cin >> T;
	ofstream out("output.out");
	for (int i = 0; i < T; i++)
	{
		int temp, r1, r2, card;
		int options[4];
		int options2[4];
		int y = 0;
		std::cin >> r1;
		int ignored = (r1 - 1) * 4;
		for (int j = 0; j < ignored; j++)
			std::cin >> temp;
		for (int j = 0; j < 4; j++)
			std::cin >> options[j];
		for (int j = 0; j < 12 - ignored; j++)
			std::cin >> temp;
		std::cin >> r2;
		ignored = (r2 - 1) * 4;
		for (int j = 0; j < ignored; j++)
			std::cin >> temp;
		for (int j = 0; j < 4; j++)
			std::cin >> options2[j];
		for (int j = 0; j < 12 - ignored; j++)
			std::cin >> temp;
		//compare rows
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (options[j] == options2[k])
				{
					y++;
					card = options[j];
				}
			}
		}
		out << "Case #" << i + 1 << ": ";
		if (y == 1)
			out << card;
		else if (y == 0)
			out << "Volunteer cheated!";
		else out << "Bad magician!";
		if (i != T - 1)
			out << "\n";
	}
	out.close();
	return 0;
}