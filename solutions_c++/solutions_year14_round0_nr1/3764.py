#include<iostream>
#include<fstream>
using namespace std;

void main()
{
	int T, ans_1, ans_2, grid_1[4][4], grid_2[4][4], k=0;
	char line[15], digit[3];

	ifstream ifile("A-small-attempt0.in");
	ofstream ofile("output.out");

	ifile.getline(line, 15);
	T = atoi(line);

	for (int testCase = 1; testCase <= T; testCase++)
	{
		ifile.getline(line, 15);
		ans_1 = atoi(line);

		for (int row= 0; row < 4; row++)
		{
			ifile.getline(line, 15);
			for (int i = 0, col=0; line[i]!='\0';col++)
			{
				k = 0;
				while (line[i] != ' ' && line[i] != '\0')
				{
					digit[k] = line[i];
					i++; k++;
				}
				digit[k] = '\0';
				grid_1[row][col] = atoi(digit);
				if (line[i] != '\0') i++;
			}
		}

		ifile.getline(line, 15);
		ans_2 = atoi(line);
		for (int row = 0; row < 4; row++)
		{
			ifile.getline(line, 15);
			for (int i = 0, col = 0; line[i] != '\0'; col++)
			{
				k = 0;
				while (line[i] != ' ' && line[i] != '\0')
				{
					digit[k] = line[i];
					i++; k++;
				}
				digit[k] = '\0';
				grid_2[row][col] = atoi(digit);
				if (line[i] != '\0') i++;
			}
		}

		//---------------MAGIC--------------

		int count = 0, find[4];
		for (int i = 0; i < 4; i++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (grid_1[ans_1 - 1][i] == grid_2[ans_2 - 1][k])
				{
					find[count] = grid_1[ans_1 - 1][i];
					count++;
				}
			}
		}

		ofile << "Case #" << testCase << ": ";

		if (count == 0)
			ofile << "Volunteer cheated!\n";
		else if (count == 1)
			ofile << find[0]<<endl;
		else
			ofile << "Bad magician!\n";
	}
	ofile.close();
}