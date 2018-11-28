#include <iostream>
#include <fstream>

using namespace std;

int check(char arr[4][4])
{
	int out = 0;
	for(int j=0;j<4;j++)
	{
		if((arr[j][0]=='X' || arr[j][0]=='T') && (arr[j][1]=='X' || arr[j][1]=='T') && (arr[j][2]=='X' || arr[j][2]=='T') && (arr[j][3]=='X' || arr[j][3]=='T'))
		{
			out = 1;
			break;
		}
		if((arr[j][0]=='O' || arr[j][0]=='T') && (arr[j][1]=='O' || arr[j][1]=='T') && (arr[j][2]=='O' || arr[j][2]=='T') && (arr[j][3]=='O' || arr[j][3]=='T'))
		{
			out = 2;
			break;
		}
	}
	if(out == 0)
	{
		for(int k=0;k<4;k++)
		{
			if((arr[0][k]=='X' || arr[0][k]=='T') && (arr[1][k]=='X' || arr[1][k]=='T') && (arr[2][k]=='X' || arr[2][k]=='T') && (arr[3][k]=='X' || arr[3][k]=='T'))
			{
				out = 1;
				break;
			}
			if((arr[0][k]=='O' || arr[0][k]=='T') && (arr[1][k]=='O' || arr[1][k]=='T') && (arr[2][k]=='O' || arr[2][k]=='T') && (arr[3][k]=='O' || arr[3][k]=='T'))
			{
				out = 2;
				break;
			}
		}
	}
	if(out==0)
	{
		if((arr[0][0]=='X' || arr[0][0]=='T') && (arr[1][1]=='X' || arr[1][1]=='T') && (arr[2][2]=='X' || arr[2][2]=='T') && (arr[3][3]=='X' || arr[3][3]=='T'))
		{
			out = 1;
		}
		else if((arr[0][3]=='X' || arr[0][3]=='T') && (arr[1][2]=='X' || arr[1][2]=='T') && (arr[2][1]=='X' || arr[2][1]=='T') && (arr[3][0]=='X' || arr[3][0]=='T'))
		{
			out = 1;
		}
		else if((arr[0][0]=='O' || arr[0][0]=='T') && (arr[1][1]=='O' || arr[1][1]=='T') && (arr[2][2]=='O' || arr[2][2]=='T') && (arr[3][3]=='O' || arr[3][3]=='T'))
		{
			out = 2;
		}
		else if((arr[0][3]=='O' || arr[0][3]=='T') && (arr[1][2]=='O' || arr[1][2]=='T') && (arr[2][1]=='O' || arr[2][1]=='T') && (arr[3][0]=='O' || arr[3][0]=='T'))
		{
			out = 2;
		}
		else 
		{
			out = 3;
			int j=0,k=0;
			while(j<4 && out==3)
			{
				while(k<4 && out==3)
				{
					if(arr[j][k]=='.')
						out=4;
					k++;
				}
				j++;
			}
		}
	}

	return out;
}

int main()
{
	std::ifstream infile;
	infile.open("A-small-attempt0.in");
	std::ofstream outfile;
	outfile.open("A-small-attempt0out.txt");

	int T;
	int out=0; //0=undetermined, 1=X won, 2=O won, 3=Draw, 4=Not completed
	char input[4][4];

	infile >> T;
	for(int i=0;i<T;i++)
	{
		out = 0;
		int j=0,k=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				infile >> input[j][k];
			}
		}
		if (out==0)
		{
			out = check(input);
		}

		outfile << "Case #" << i+1 << ": ";
		switch (out)
		{
			case 1:
				outfile << "X won" << endl;
				break;
			case 2:
				outfile << "O won" << endl;
				break;
			case 3:
				outfile << "Draw" << endl;
				break;
			case 4:
				outfile << "Game has not completed" << endl;
				break;
			default:
				outfile << "bug" << endl;
				break;
		}
	}
	infile.close();
	outfile.close();
	return 0;
}