#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");
	int T;
	in >> T;

	for(int i = 0; i < T; ++i)
	{
		int row1, row2;
		in >> row1;
		--row1;

		int cards1[4][4], cards2[4][4];

		for(int j = 0; j < 4; ++j)
		for(int k = 0; k < 4; ++k)
			in >> cards1[j][k];

		in >> row2;
		--row2;

		for(int j = 0; j < 4; ++j)
		for(int k = 0; k < 4; ++k)
			in >> cards2[j][k];

		int match = -1;
		for(int j = 0; j < 4; ++j)
		for(int k = 0; k < 4; ++k)
		{
			if(cards1[row1][j] == cards2[row2][k])
			{
				if(match == -1)
					match = cards1[row1][j];
				else if(match >= 0)
					match = -2;
				else
					match = -2;
			}
		}

		out << "Case #" << (i + 1) << ": ";

		if(match == -1)
			out << "Volunteer cheated!" << std::endl;
		else if(match == -2)
			out << "Bad magician!" << std::endl;
		else
			out << match << std::endl;
	}

	return 0;
}

