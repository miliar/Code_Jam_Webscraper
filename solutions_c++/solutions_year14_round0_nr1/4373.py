#include <fstream>
using namespace std;

void readGrid(int * grid, ifstream &fin)
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j ++)
		{
			fin>>grid[i*4+j];
		}
	}
}

void problem1()
{
	ifstream fin("input1.txt");
	ofstream fout("output1.txt");
	int numcases;
	int row1,row2;
	int grid1[16];
	int grid2[16];
	fin>>numcases;

	for (int i=0;i<numcases;i++)
	{
		fin>>row1;
		row1--;
		readGrid(grid1, fin);
		fin>>row2;
		row2--;
		readGrid(grid2, fin);

		int matchCount = 0;
		int matchNumber;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (grid1[row1*4 + j] == grid2[row2*4 + k])
				{
					matchCount++;
					matchNumber = grid1[row1*4 + j];
				}
			}
		}

		fout<<"Case #"<<i + 1<<": ";

		if (matchCount == 1)
		{
			fout<<matchNumber;
		}
		else if (matchCount == 0)
		{
			fout<<"Volunteer cheated!";
		}
		else
		{
			fout <<"Bad magician!";
		}
		fout<<endl;
	}
}

void main()
{

	problem1();
}

