// MagicTrick.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>

using namespace std;


int Data1[4][4];
int Data2[4][4];
int T;
int choose1;
int choose2;
int count;
int chooseNum;
int main(void)
{
	ifstream fin("A-small-attempt3.in");
	ofstream fout("MagicTrickOutput.txt");
	
	fin>>T;

	for (int t = 0; t < T; t++)
	{
		chooseNum = 0;
		choose1 = 0;
		choose2 = 0; 
		count = 0;
		fin>>choose1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin>>Data1[i][j];
			}
		}

		fin>>choose2;
		for (int h = 0; h < 4; h++)
		{
			for (int k = 0; k < 4; k++)
			{
				fin>>Data2[h][k];
			}
		}
		
		for (int l = 0; l < 4; l++)
		{
			int tmp = Data1[choose1-1][l];
			for (int m = 0; m < 4; m++)
			{
				if (tmp == Data2[choose2-1][m])
				{
					count++;
					chooseNum = tmp;
				}
			}
		}
		
		if (1 == count)
		{
			fout<<"Case \#"<<t+1<<": "<<chooseNum<<endl;
		}
		else if (0 == count)
		{
			fout<<"Case \#"<<t+1<<": Volunteer cheated!"<<endl;
		}
		else if (count > 1)
		{
			fout<<"Case \#"<<t+1<<": Bad magician!"<<endl;
			
		}

		
	}

	fin.close();
	fout.close();

	return 0;
}
