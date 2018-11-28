
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include "string"


using namespace std;


int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	int T;
	fin>>T;




	for (int test =0; test< T ; test++)
	{
		fout<<"Case #"<<test+1<<": ";
		int skew = 0, diagonal=0;
		int row[4];
		int col[4];
		bool dot = false;
		string S[4];

		for (int i =0; i< 4 ; i++)
		{
			if (i == 0)
			{
				for (int j =0; j< 4 ; j++)
				{
					col[j] = 0;
				}
			}
			row[i] = 0;

			fin>>S[i];
	

			for (int j =0; j< 4 ; j++)
			{
				if (S[i][j] == 'O')
				{
					row[i]++;
					col[j]++;
					if (i == j)
					{
						diagonal++;
					}
					if (i+j == 3)
					{
						skew++;
					}
				}
				else if (S[i][j] == 'X')
				{
					row[i]--;
					col[j]--;
					if (i == j)
					{
						diagonal--;
					}
					if (i+j == 3)
					{
						skew--;
					}
				}
				else if (S[i][j] == 'T')
				{
				   col[i]+=10;
				   row[i]+=10;
				   if (i == j)
					{
						diagonal+=10;
					}
				   if (i+j == 3)
					{
						skew+=10;
					}
				}
				else if (S[i][j] == '.')
				dot = true;
			}

		}
		
		if (skew == 4 || skew ==13 || diagonal== 4 || diagonal == 13 || 
			row[0] == 4 || row[0] == 13 ||row[1] == 4 ||row[1] == 13 ||
			row[2] == 4 || row[2] == 13 ||row[3] == 4 ||row[3] == 13 ||
			col[0] == 4 || col[0] == 13 ||col[1] == 4 ||col[1] == 13 ||
			col[2] == 4 || col[2] == 13 ||col[3] == 4 ||col[3] == 13)
		{
			fout<<"O won"<<endl;
		}
		else if (skew == -4 || skew ==7 || diagonal== -4 || diagonal == 7 || 
			row[0] == -4 || row[0] == 7 ||row[1] == -4 ||row[1] == 7 ||
			row[2] == -4 || row[2] == 7 ||row[3] == -4 ||row[3] == 7 ||
			col[0] == -4 || col[0] == 7 ||col[1] == -4 ||col[1] == 7 ||
			col[2] == -4 || col[2] == 7 ||col[3] == -4 ||col[3] == 7)
		{
			fout<<"X won"<<endl;
		}
		else if (dot)
			fout<<"Game has not completed"<<endl;
		else fout<<"Draw"<<endl;
	}
	
	return 0;
}