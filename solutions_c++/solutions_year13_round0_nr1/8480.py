#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
using namespace std;
char ans;
char a[5][5];
bool check(int x,int y,char symbol)
{
	if(a[x][y]==symbol || a[x][y]=='T')
		return true;
	return false;
}
void tictactoe(int x,int y,char symbol)
{
	if(x==1 || y==1)
	{
		if((check(1,1,symbol) && check(2,2,symbol) && check(3,3,symbol) && check(4,4,symbol)))
			ans=symbol;
		else
			if(check(4,1,symbol) && check(3,2,symbol) && check(2,3,symbol) && check(1,4,symbol))
				ans=symbol;
			else

		if(x==1)
		{
			if(check(x,y,symbol) && check(x+1,y,symbol) && check(x+2,y,symbol) && check(x+3,y,symbol))
			
			{
				ans=symbol;
			}
		}
		if(y==1)
		{ 
			if(check(x,y,symbol) && check(x,y+1,symbol) && check(x,y+2,symbol) && check(x,y+3,symbol))
			{
				ans=symbol;
			}
		}
	}

}
bool isempty()
{
	int i,j;
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			if(a[i][j]=='.')
				return true;
	return false;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t,i,j,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				cin>>a[i][j];
			}
		ans='1';
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				if(a[i][j]=='X' || a[i][j]=='O')
				tictactoe(i,j,a[i][j]);
			}
		if(ans=='1')
		{
			if(isempty())
			{
				cout<<"Case #"<<k<<": Game has not completed"<<endl;

			}
			else
				cout<<"Case #"<<k<<": Draw"<<endl;
		}
		else
		{
			if(ans=='X')
			{
				cout<<"Case #"<<k<<": X won"<<endl;
			}
			else
				cout<<"Case #"<<k<<": O won"<<endl;
		}
	}
	return 0;
}




