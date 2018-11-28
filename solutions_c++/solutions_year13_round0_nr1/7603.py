#include<iostream>
using namespace std;

char board[5][5];
int row[5];
int col[5];
int diagonal[3];

int main(int argc,char* argv[])
{
	int i,j,k,T,flag=0,tag=0;;
	cin>>T;
	for(k=1;k<=T;k++)
	{
		for(i=1;i<5;i++) row[i]=col[i]=0;
		for(i=1;i<3;i++) diagonal[i]=0;
		flag=0;tag=0;
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
				cin>>board[i][j];
			for(i=1;i<5;i++)
			{
				for(j=1;j<5;j++)
				{
					if(board[i][j]=='X') row[i]++;
					else if(board[i][j]=='O') row[i]--;
					else if(board[i][j]=='T') continue;
					else
					{
						tag=1;
						row[i]=-10;
					}
				}
				if(row[i]==3||row[i]==4) 
				{
					cout<<"Case #"<<k<<": X won"<<endl;
					flag=1;
					break;
				}
				if(row[i]==-3||row[i]==-4) 
				{
					cout<<"Case #"<<k<<": O won"<<endl;
					flag=1;
					break;
				}
			}
			if(flag) continue;
			for(j=1;j<5;j++)
			{
				for(i=1;i<5;i++)
				{
					if(board[i][j]=='X') col[j]++;
					else if(board[i][j]=='O') col[j]--;
					else if(board[i][j]=='T') continue;
					else 
					{
						tag=1;
						col[j]=-10;
					}
				}
				if(col[j]==3||col[j]==4) 
				{
					cout<<"Case #"<<k<<": X won"<<endl;
					flag=1;
					break;
				}
				if(col[j]==-3||col[j]==-4) 
				{
					cout<<"Case #"<<k<<": O won"<<endl;
					flag=1;
					break;
				}
			}
			if(flag) continue;
			for(i=1;i<5;i++)
			{
				if(board[i][i]=='X')  diagonal[1]++;
				else if(board[i][i]=='O')  diagonal[1]--;
				else if(board[i][i]=='T') continue;
				else 
				{
					tag=1;
					diagonal[1]=-10;
				}
			}
			for(i=1,j=4;i<5;i++,j--)
			{
				if(board[i][j]=='X')  diagonal[2]++;
				else if(board[i][j]=='O')  diagonal[2]--;
				else if(board[i][j]=='T') continue;
				else 
				{
					tag=1;
					diagonal[2]=-10;
				}
			}
			for(j=1;j<3;j++)
			{
				if(diagonal[j]==3||diagonal[j]==4) 
				{
					cout<<"Case #"<<k<<": X won"<<endl;
					flag=1;
					break;
				}
				if(diagonal[j]==-3||diagonal[j]==-4) 
				{
					cout<<"Case #"<<k<<": O won"<<endl;
					flag=1;
					break;
				}
			}
			if(flag) continue;
			if(tag) cout<<"Case #"<<k<<": Game has not completed"<<endl;	
			else  cout<<"Case #"<<k<<": Draw"<<endl;
	}
	return 0;
}