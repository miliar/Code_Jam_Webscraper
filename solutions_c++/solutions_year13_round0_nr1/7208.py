#include<iostream>
#include<fstream>
#include<cstdio>
#define SIZE 4
#define l_int long int
using namespace std;
char matrix[SIZE][SIZE];


char check()
{
	int i;
	/* check rows */
	for(i=0;i<SIZE;i++)
	{
		if(matrix[i][0]=='X' && matrix[i][1]=='X' && matrix[i][2]=='X' && matrix[i][3]=='X')
			return 'X';
		if(matrix[i][0]=='X' && matrix[i][1]=='X' && matrix[i][2]=='X' && matrix[i][3]=='T')
			return 'X';
		if(matrix[i][0]=='X' && matrix[i][1]=='X' && matrix[i][2]=='T' && matrix[i][3]=='X')
			return 'X';
		if(matrix[i][0]=='X' && matrix[i][1]=='T' && matrix[i][2]=='X' && matrix[i][3]=='X')
			return 'X';
		if(matrix[i][0]=='T' && matrix[i][1]=='X' && matrix[i][2]=='X' && matrix[i][3]=='X')
			return 'X';

		if(matrix[i][0]=='O' && matrix[i][1]=='O' && matrix[i][2]=='O' && matrix[i][3]=='O')
			return 'O';
		if(matrix[i][0]=='O' && matrix[i][1]=='O' && matrix[i][2]=='O' && matrix[i][3]=='T')
			return 'O';
		if(matrix[i][0]=='O' && matrix[i][1]=='O' && matrix[i][2]=='T' && matrix[i][3]=='O')
			return 'O';
		if(matrix[i][0]=='O' && matrix[i][1]=='T' && matrix[i][2]=='O' && matrix[i][3]=='O')
			return 'O';
		if(matrix[i][0]=='T' && matrix[i][1]=='O' && matrix[i][2]=='O' && matrix[i][3]=='O')
			return 'O';
	}

	/* check columns */
	for(i=0;i<SIZE;i++)
	{
		if(matrix[0][i]=='X' && matrix[1][i]=='X' && matrix[2][i]=='X' && matrix[3][i]=='X')
			return 'X';
		if(matrix[0][i]=='X' && matrix[1][i]=='X' && matrix[2][i]=='X' && matrix[3][i]=='T')
			return 'X';
		if(matrix[0][i]=='X' && matrix[1][i]=='X' && matrix[2][i]=='T' && matrix[3][i]=='X')
			return 'X';
		if(matrix[0][i]=='X' && matrix[1][i]=='T' && matrix[2][i]=='X' && matrix[3][i]=='X')
			return 'X';
		if(matrix[0][i]=='T' && matrix[1][i]=='X' && matrix[2][i]=='X' && matrix[3][i]=='X')
			return 'X';

		if(matrix[0][i]=='O' && matrix[1][i]=='O' && matrix[2][i]=='O' && matrix[3][i]=='O')
			return 'O';
		if(matrix[0][i]=='O' && matrix[1][i]=='O' && matrix[2][i]=='O' && matrix[3][i]=='T')
			return 'O';
		if(matrix[0][i]=='O' && matrix[1][i]=='O' && matrix[2][i]=='T' && matrix[3][i]=='O')
			return 'O';
		if(matrix[0][i]=='O' && matrix[1][i]=='T' && matrix[2][i]=='O' && matrix[3][i]=='O')
			return 'O';
		if(matrix[0][i]=='T' && matrix[1][i]=='O' && matrix[2][i]=='O' && matrix[3][i]=='O')
			return 'O';

	}

	/* check diagonals */

	/*  diagonal 1 */
	if(matrix[0][0]=='X' && matrix[1][1]=='X' && matrix[2][2]=='X' && matrix[3][3]=='X')
			return 'X';
	if(matrix[0][0]=='X' && matrix[1][1]=='X' && matrix[2][2]=='X' && matrix[3][3]=='T')
			return 'X';
	if(matrix[0][0]=='X' && matrix[1][1]=='X' && matrix[2][2]=='T' && matrix[3][3]=='X')
			return 'X';
	if(matrix[0][0]=='X' && matrix[1][1]=='T' && matrix[2][2]=='X' && matrix[3][3]=='X')
			return 'X';
	if(matrix[0][0]=='T' && matrix[1][1]=='X' && matrix[2][2]=='X' && matrix[3][3]=='X')
			return 'X';

	if(matrix[0][0]=='O' && matrix[1][1]=='O' && matrix[2][2]=='O' && matrix[3][3]=='O')
			return 'O';
	if(matrix[0][0]=='O' && matrix[1][1]=='O' && matrix[2][2]=='O' && matrix[3][3]=='T')
			return 'O';
	if(matrix[0][0]=='O' && matrix[1][1]=='O' && matrix[2][2]=='T' && matrix[3][3]=='O')
			return 'O';
	if(matrix[0][0]=='O' && matrix[1][1]=='T' && matrix[2][2]=='O' && matrix[3][3]=='O')
			return 'O';
	if(matrix[0][0]=='T' && matrix[1][1]=='O' && matrix[2][2]=='O' && matrix[3][3]=='O')
			return 'O';


	/*  diagonal 2 */
	if(matrix[0][3]=='X' && matrix[1][2]=='X' && matrix[2][1]=='X' && matrix[3][0]=='X')
			return 'X';
	if(matrix[0][3]=='X' && matrix[1][2]=='X' && matrix[2][1]=='X' && matrix[3][0]=='T')
			return 'X';
	if(matrix[0][3]=='X' && matrix[1][2]=='X' && matrix[2][1]=='T' && matrix[3][0]=='X')
			return 'X';
	if(matrix[0][3]=='X' && matrix[1][2]=='T' && matrix[2][1]=='X' && matrix[3][0]=='X')
			return 'X';
	if(matrix[0][3]=='T' && matrix[1][2]=='X' && matrix[2][1]=='X' && matrix[3][0]=='X')
			return 'X';

	if(matrix[0][3]=='O' && matrix[1][2]=='O' && matrix[2][1]=='O' && matrix[3][0]=='O')
			return 'O';
	if(matrix[0][3]=='O' && matrix[1][2]=='O' && matrix[2][1]=='O' && matrix[3][0]=='T')
			return 'O';
	if(matrix[0][3]=='O' && matrix[1][2]=='O' && matrix[2][1]=='T' && matrix[3][0]=='O')
			return 'O';
	if(matrix[0][3]=='O' && matrix[1][2]=='T' && matrix[2][1]=='O' && matrix[3][0]=='O')
			return 'O';
	if(matrix[0][3]=='T' && matrix[1][2]=='O' && matrix[2][1]=='O' && matrix[3][0]=='O')
			return 'O';


	/* check Game has not completed case */
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(matrix[i][j]=='.')
				return 'N';
		}
	}

	return 'D';
}
int main()
{
	int T;

	ifstream infile;
	ofstream outfile;
  	infile.open("A-large.in");
  	outfile.open("a-output.out");
  	if (infile.is_open())
	{

	  		infile>>T;
	  		int k=1;
	  		while(T--)
	  		{
	  			for(int i=0;i<4;i++)
	  			{
	  				for(int j=0;j<4;j++)
	  				{
	  					infile>>matrix[i][j];
	  				}
	  			}

	  			char result=check();
	  			if(result=='X')
	  				outfile<<"Case #"<<k++<<": X won"<<endl;
	  			if(result=='O')
	  				outfile<<"Case #"<<k++<<": O won"<<endl;
	  			if(result=='D')
	  				outfile<<"Case #"<<k++<<": Draw"<<endl;
	  			if(result=='N')
	  				outfile<<"Case #"<<k++<<": Game has not completed"<<endl;

	  		}


	}
	infile.close();
	outfile.close();
  return 0;
}
