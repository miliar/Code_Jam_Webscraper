#include <iostream>
#include <fstream>
using namespace std;

int main(void)
{
	ifstream infile;
	infile.open("A-large.in.txt");
	ofstream outfile ("A-large.out");
	int T = 0;
	infile >> T;
	char waste[4];
	for (int i = 0; i < T; i++)
	{
		char grid[4][4];
		//infile.get(waste[0]);
		/*for (int ii = 0; ii < 4; ii++)
		{
			for (int iii = 0; iii < 4; iii++)
				infile.get(grid[ii][iii]);
		}*/
		/*infile.getline(grid[0], 5);
		infile.getline(grid[1], 5);
		infile.getline(grid[2], 5);
		infile.getline(grid[3], 5);*/
		infile >> grid[0];
		//cout << grid[0] << "\n";
		infile >> grid[1];
		//cout << grid[1] << "\n";
		infile >> grid[2];
		//cout << grid[2] << "\n";
		infile >> grid[3];
		//cout << grid[3] << "\n";
		//Flag Values: 0 - not yet completed, 1 - draw, 2 - o wins, 3 - x wins
		int flag = 1;
		for (int j = 0; j < 4; j++)
		{
			if ((grid[j][0] == 'O' || grid[j][0] == 'T') && (grid[j][1] == 'O' || grid[j][1] == 'T') && (grid[j][2] == 'O' || grid[j][2] == 'T') && (grid[j][3] == 'O' || grid[j][3] == 'T'))
			{
				flag = 2;
				goto end;
			}
			if ((grid[j][0] == 'X' || grid[j][0] == 'T') && (grid[j][1] == 'X' || grid[j][1] == 'T') && (grid[j][2] == 'X' || grid[j][2] == 'T') && (grid[j][3] == 'X' || grid[j][3] == 'T'))
			{
				flag = 3;
				goto end;
			}
			if (grid[j][0] == '.' || grid[j][1] == '.' || grid[j][2] == '.' || grid[j][3] == '.')
				flag = 0;
		}
		
		for (int k = 0; k < 4; k++)
		{
			if ((grid[0][k] == 'O' || grid[0][k] == 'T') && (grid[1][k] == 'O' || grid[1][k] == 'T') && (grid[2][k] == 'O' || grid[2][k] == 'T') && (grid[3][k] == 'O' || grid[3][k] == 'T'))
			{
				flag = 2;
				/*if (i == 3)
					cout << "p\n";*/
				goto end;
			}
			if ((grid[0][k] == 'X' || grid[0][k] == 'T') && (grid[1][k] == 'X' || grid[1][k] == 'T') && (grid[2][k] == 'X' || grid[2][k] == 'T') && (grid[3][k] == 'X' || grid[3][k] == 'T'))
			{
				flag = 3;
				goto end;
			}
		}
		
		
		if ((grid[0][0] == 'O' || grid[0][0] == 'T') && (grid[1][1] == 'O' || grid[1][1] == 'T') && (grid[2][2] == 'O' || grid[2][2] == 'T') && (grid[3][3] == 'O' || grid[3][3] == 'T'))
		{
			flag = 2;
			goto end;
		}
		if ((grid[0][0] == 'X' || grid[0][0] == 'T') && (grid[1][1] == 'X' || grid[1][1] == 'T') && (grid[2][2] == 'X' || grid[2][2] == 'T') && (grid[3][3] == 'X' || grid[3][3] == 'T'))
		{
			flag = 3;
			goto end;
		}
		
		if ((grid[0][3] == 'O' || grid[0][3] == 'T') && (grid[1][2] == 'O' || grid[1][2] == 'T') && (grid[2][1] == 'O' || grid[2][1] == 'T') && (grid[3][0] == 'O' || grid[3][0] == 'T'))
		{
			flag = 2;
			goto end;
		}
		
		if ((grid[0][3] == 'X' || grid[0][3] == 'T') && (grid[1][2] == 'X' || grid[1][2] == 'T') && (grid[2][1] == 'X' || grid[2][1] == 'T') && (grid[3][0] == 'X' || grid[3][0] == 'T'))
		{
			flag = 3;
			goto end;
		}
		
		end:
			outfile << "Case #" << i+1 << ": ";
			switch (flag)
			{
				case 0:
					outfile << "Game has not completed\n";
					break;
				case 1:
					outfile << "Draw\n";
					break;
				case 2:
					outfile << "O won\n";
					break;
				case 3:
					outfile << "X won\n";
					break;
			}
			//infile.get(waste[0]);
	}
	
	infile.close();
	outfile.close();
	
	return 0;
}