
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void main()
{
	fstream file;
	fstream out;
	int linect = -1;

	int user1;
	int user2;
	int caseno = 1;

	string temp;

	int grid1[4][4];
	int grid2[4][4];



	file.open("A-small-attempt0.in");
	out.open("out.txt");


	while (getline(file, temp))
	{
		switch (linect)
		{

		case -1:
			linect = 0;
			continue;


		case  0:
			istringstream(temp) >> user1;
			linect ++;
			for (int i = 0; i < 4; ++i)
			{
				file >> grid1[0][i];
			}
			continue;

		case  1:
			for (int i = 0; i < 4; ++i)
			{
				file >> grid1[1][i];
			}
			linect ++;
			continue;

		case 2:
			for (int i = 0; i < 4; i++)
			{
				file >> grid1[2][i];
			}
			linect ++;
			continue;

		case 3:
			for (int i = 0; i < 4; i++)
			{
				file >> grid1[3][i];
			}
			linect ++;
			continue;

		case  4:
			file >> user2;
			linect ++;
			cout << "\n";
			continue;

		case 5:
			for (int i = 0; i < 4; i++)
			{
				file >> grid2[0][i];
			}
			linect ++;
			continue;


		case 6:
			for (int i = 0; i < 4; i++)
			{
				file >> grid2[1][i];
			}
			linect ++;
			continue;

		case 7:
			for (int i = 0; i < 4; i++)
			{
				file >> grid2[2][i];
			}
			linect ++;
			continue;

		case 8:
			for (int i = 0; i < 4; i++)
			{
				file >> grid2[3][i];
			}
			linect ++;
			continue;

		case 9:

			int no = -1;
			int final;

			for (int m = 0; m < 4; m++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (grid1[user1 - 1][m] == grid2[user2 - 1][j])
					{
						final = j;
						no ++;
					}
				}
			}

			if (no == 0)
			{
				out << "Case #" << caseno << ": " << grid2[user2 - 1][final] << "\n";
				caseno ++;
			}

			if (no > 0)
			{
				out << "Case #" << caseno << ": " << "Bad magician!" << "\n";
				caseno ++;
			}

			if (no < 0)
			{
				out << "Case #" << caseno << ": " << "Volunteer cheated!" << "\n";
				caseno ++;
			}

			linect = 0;
			cout << "\n";
			continue;
		}
	}
	file.close();

}