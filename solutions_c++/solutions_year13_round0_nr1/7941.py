/*
BHARATHKUMAR
13-4-13
C++
*/
#include<iostream>
using namespace std;

class A
{
char game[4][4];

public: 
void process()
{

char flag='.';
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
cin>>game[i][j];
char R=check();
if(R=='Y')
cout<<"Game has not completed"<<endl;
else if(R=='D')
cout<<"Draw"<<endl;
else
cout<<R<<" won"<<endl;
}
char check()
{
	
	char flag='.';
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
		if(game[i][j]!='.')
		{
			if(flag=='.')
			{
			if(checkhv(i,j))
			{
				flag=game[i][j];
				j=4;
				i=4;
			}
			else if(checkd(i,j))
			{
				flag=game[i][j];
				j=4;
				i=4;
			}
			}
		}
	if(flag=='.' && checkdot())
		return 'Y';
	else if(flag=='.')
		return 'D';
	else
		return flag;
}

int checkhv(int x,int y)
{
	int flag=1;
	for(int i=x+1;i<4 && i<4+x;i++)
		if(game[i][y]==game[x][y] || game[i][y]=='T')
			flag++;
	if(flag==4)
		return 1;
	flag=1;
	for(int j=y+1;j<4 && j<4+y;j++)
		if(game[x][j]==game[x][y] || game[x][j]=='T')
			flag++;
	if(flag==4)
		return 1;
	else
		return 0;
}

int checkd(int x,int y)
{
	int flag=1,i,j;
	for(i=x+1,j=y+1;i<4 && i<4+x;i++,j++)
		if(j<4 && (game[i][j]==game[x][y] || game[i][j]=='T'))
			flag++;
	if(flag==4)
		return 1;
	flag=1;
	for(i=x+1,j=y-1;i<4 && i<4+x;i++,j--)
		if(j>=0 && (game[i][j]==game[x][y] || game[i][j]=='T'))
			flag++;
	if(flag==4)
		return 1;
	else
		return 0;
}

int checkdot()
{
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
		if(game[i][j]=='.')
			return 1;
	return 0;
}
	
};

int main()
{
int T;
A a;
cin>>T;
for(int i=0;i<T;i++)
{
cout<<"Case #"<<i+1<<": ";
a.process();
}
}
