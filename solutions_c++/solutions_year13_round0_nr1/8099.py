#include<iostream>
#include<string>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	char board [4][4];
	int test,x,o,count1=0,count2=0,u=0;
	cin>>test;
	for(int t=0;t<test;t++)
	{
		for(int m=0;m<4;m++)
		{ 
			for(int k=0;k<4;k++)
			{
				cin>>board[m][k];  
				if( board[m][k] == 'X')
					count1++;
				else if(board[m][k] == 'T')
					u++;
				else if( board[m][k]== 'O' )
					count2++;
				else if(board[m][k] == 'T')
					u++;

			}  

		}

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<1;j++)
			{
				if(board[i][j] == board[i][j+1] && board[i][j+1] == board[i][j+2] && board[i][j+2] == board[i][j+3] && board[i][j+3] != 'O' && board[i][j+3] !='.' )
					x=1;
				else if(board[i][j] == board[i][j+1] && board[i][j+1] == board[i][j+2] && board[i][j+2] == board[i][j+3] && board[i][j+3] != 'X' && board[i][j+3] !='.' )
					o =2;
			}
		}
		for(int i=0;i<1;i++)
		{
			for(int j=0;j<4;j++)

			{
				if( board[i][j] == board[i+1][j] && board[i+1][j] == board[i+2][j] && board[i+2][j] == board[i+3][j] && board[i+3][j] != 'O' && board[i+3][j] != '.')
					x=1;
				else if( board[i][j] == board[i+1][j] && board[i+1][j] == board[i+2][j] && board[i+2][j] == board[i+3][j] && board[i+3][j] != 'X' && board[i+3][j] != '.' )
					o =2;
			}
		}
		if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == board[3][3] &&  board[3][3] != 'O' && board[3][3] != '.' )
			x=1;

		else if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == board[3][3] &&  board[3][3] != 'X' && board[3][3] != '.' )
			o=2;

		else if (board[0][3] == board[1][2] && board[1][2] == board[2][1] && board[2][1] == board[3][0] && board[3][0] != 'O' && board[3][0]  != '.' )
			x=1;
		else if (board[0][3] == board[1][2] && board[1][2] == board[2][1] && board[2][1] == board[3][0] && board[3][0] != 'X' && board[3][0] != '.' )
			o=2;



		if(x == 1 && o != 2) 
			cout<<"Case #"<<t+1<<": X won"<<endl;
		else if(o == 2 && x != 1)
			cout<<"Case #"<<t+1<<": O won"<<endl;
		else if( count1+u >= 8 && u+count2 >= 8)
			cout<<"Case #"<<t+1<<": Draw"<<endl;
		else if (count1 == 8  && count2 == 8)
			cout<<"Case #"<<t+1<<": Draw"<<endl;
		else if(count1 == 0 && count2 == 0 && u == 0)
			cout<<"Case #"<<t+1<<": Game has not completed"<<endl;
		else
			cout<<"Case #"<<t+1<<": Game has not completed"<<endl;
		x=0,o=0,count1=0,count2=0,u=0;
		if(t==test-1)
			cout<<'\n';

	}
}