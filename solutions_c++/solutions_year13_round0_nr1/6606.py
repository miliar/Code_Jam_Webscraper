#include<iostream>
#include<fstream>
#include<string>
using namespace std;
bool IsX( char arr[],int n)
{
	if((arr[0]=='X'||arr[0]=='T')&&(arr[1]=='X'||arr[1]=='T')&&(arr[2]=='X'||arr[2]=='T')&&(arr[3]=='X'||arr[3]=='T'))
		return true;
	else return false;
}

bool IsY( char arr[],int n)
{
	if((arr[0]=='O'||arr[0]=='T')&&(arr[1]=='O'||arr[1]=='T')&&(arr[2]=='O'||arr[2]=='T')&&(arr[3]=='O'||arr[3]=='T'))
		return true;
	else return false;
}
bool IsDot(char arr[4][4])
{
	for(int i=0;i<4;i++)
		for (int j = 0; j < 4; j++)
			if(arr[i][j]=='.')
				return true;
	return false;
}
bool IsCrossO(char arr[4][4])
{
	if((arr[0][0]=='O'||arr[0][0]=='T')&&(arr[1][1]=='O'||arr[1][1]=='T')&&(arr[2][2]=='O'||arr[2][2]=='T')&&(arr[3][3]=='O'||arr[3][3]=='T')||(arr[0][3]=='O'||arr[0][3]=='T')&&(arr[1][2]=='O'||arr[1][2]=='T')&&(arr[2][1]=='O'||arr[2][1]=='T')&&(arr[3][0]=='O'||arr[3][0]=='T'))
		return true;
	return false;
}
bool IsCroosX(char arr[4][4])
{
	if((arr[0][0]=='X'||arr[0][0]=='T')&&(arr[1][1]=='X'||arr[1][1]=='T')&&(arr[2][2]=='X'||arr[2][2]=='T')&&(arr[3][3]=='X'||arr[3][3]=='T')||(arr[0][3]=='X'||arr[0][3]=='T')&&(arr[1][2]=='X'||arr[1][2]=='T')&&(arr[2][1]=='X'||arr[2][1]=='T')&&(arr[3][0]=='X'||arr[3][0]=='T'))
		return true;
	return false;
}
int main ()
{
	int n ;
	string line;
	ifstream filein("A-large.in");
	ofstream fileout("output.txt");
	bool FoundT=false,IsOut=false,IsWinnerX=false,IsWinnerY=false;
	char board[4][4],C,arr[4];
	filein>>n;
	for(int i=0; i<n; i++)
	{
		for(int j =0; j<4; j++)
			for(int k=0; k<4; k++)
			{
				filein>>C;
				board[j][k]=C;
			}
			for(int k=0; k<4; k++)
			{
				for(int m=0; m<4; m++)
				{
					arr[m]=board[k][m];
				}
				if(IsX(arr,4))
				{
					fileout<<"Case #"<<i+1<<": X won"<<endl;
					IsWinnerX=true;
					break;
				}
				else if(IsY(arr,4))
				{
					fileout<<"Case #"<<i+1<<": O won"<<endl;
					IsWinnerY=true;
					break;
				}
			}
			if(!(IsWinnerX||IsWinnerY))
			{
				for(int b=0; b<4; b++)
			{
				for(int a=0; a<4; a++)
				{
					arr[a]=board[a][b];
				}
				if(IsX(arr,4))
				{
					fileout<<"Case #"<<i+1<<": X won"<<endl;
					IsWinnerX=true;
					break;
				}
				else if(IsY(arr,4))
				{
					fileout<<"Case #"<<i+1<<": O won"<<endl;
					IsWinnerY=true;
					break;
				}
			}
			}
			if(!(IsWinnerX||IsWinnerY))
				{if(IsCroosX(board))
			{
				fileout<<"Case #"<<i+1<<": X won"<<endl;
					IsWinnerX=true;
			}
				else if(IsCrossO(board))
					{
						fileout<<"Case #"<<i+1<<": O won"<<endl;
						IsWinnerY=true;
			}
			if(!(IsWinnerX||IsWinnerY))
				if(IsDot(board))
					fileout<<"Case #"<<i+1<<": Game has not completed"<<endl;
				else
					fileout<<"Case #"<<i+1<<": Draw"<<endl;
			
			}
			IsWinnerX=IsWinnerY=false;
			getline(filein,line);
	}
	return 0;
	}