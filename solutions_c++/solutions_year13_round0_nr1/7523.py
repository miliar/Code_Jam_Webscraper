#include <iostream>
#include <string>

using namespace std;

string board[5];

int main()
{
	int T,tt=1,i,j,W;
	char k;
	bool emp;
	cin>>T;
	while(T--)
	{
		W=0;
		emp=false;
		for(i=0;i<4;i++)
		{
			cin>>board[i];
			for(j=0;j<4;j++)
			{
				
				if(board[i][j]=='O')
					board[i][j]='Y';
				else if(board[i][j]=='.')
					emp=true;
			}
		}
		for(i=0;i<4 && !W;i++)
		{
			for(k='X';k<='Y';k++)
			{
				for(j=0;j<4;j++)
					if(board[i][j]!='T' && board[i][j]!=(char)k)
						break;
				if(j==4)
					W=k+1-'X';

				for(j=0;j<4;j++)
					if(board[j][i]!='T' && board[j][i]!=k)
						break;
				if(j==4)
					W=k+1-'X';
			}
		}
		for(k='X';k<='Y';k++)
		{
			for(j=0;j<4;j++)
				if(board[j][j]!='T' && board[j][j]!=(char)k)
					break;
			if(j==4)
				W=k+1-'X';
			for(j=0;j<4;j++)
				if(board[j][3-j]!='T' && board[j][3-j]!=(char)k)
					break;
			if(j==4)
				W=k+1-'X';
		}
		cout<<"Case #"<<tt++<<": ";
		if(W==1)
			cout<<"X won\n";
		else if(W==2)
			cout<<"O won\n";
		else if(emp==true)
			cout<<"Game has not completed\n";
		else
			cout<<"Draw\n";
	}
}
