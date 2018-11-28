#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;



int main()
{
int test;
cin>>test;
for(int testno=1;testno<=test;testno++)
{
	cout<<"Case #"<<testno<<": ";
	string board[4];
	for(int j=0;j<4;j++)
	cin>>board[j];
	bool levee;
	
	
	
	levee=false;
	
	
	for(int i=0;i<4;i++)
	if((board[i][0]=='X' || board[i][0]=='T') && (board[i][1]=='X' || board[i][1]=='T')  && (board[i][2]=='X' || board[i][2]=='T') &&(board[i][3]=='X' || board[i][3]=='T') )
	levee=true;
	//cout<<levee<<endl;
	for(int i=0;i<4;i++)
	if((board[0][i]=='X' || board[0][i]=='T') &&(board[1][i]=='X' || board[1][i]=='T') && (board[2][i]=='X' || board[2][i]=='T')&& (board[3][i]=='X' || board[3][i]=='T'))
	levee=true;
	//c////out<<levee<<endl;
	if((board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T')  && (board[3][3]=='X' || board[3][3]=='T') )
	levee=true;
	//cout<<levee<<endl;
	if((board[3][0]=='X' || board[3][0]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[1][2]=='X' || board[1][2]=='T')  && (board[0][3]=='X' || board[0][3]=='T') )
	levee=true;
	//cout<<levee<<endl;
	if(levee)
	{
		cout<<"X won"<<endl;
		continue;
	}
	
	
	
	
	levee=false;
	for(int i=0;i<4;i++)
	if((board[i][0]=='O' || board[i][0]=='T') && (board[i][1]=='O' || board[i][1]=='T')  && (board[i][2]=='O' || board[i][2]=='T') &&(board[i][3]=='O' || board[i][3]=='T') )
	levee=true;
	
	for(int i=0;i<4;i++)
	if((board[0][i]=='O' || board[0][i]=='T') &&(board[1][i]=='O' || board[1][i]=='T') && (board[2][i]=='O' || board[2][i]=='T')&& (board[3][i]=='O' || board[3][i]=='T'))
	levee=true;
	
	if((board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T')  && (board[3][3]=='O' || board[3][3]=='T') )
	levee=true;
	
	if((board[3][0]=='O' || board[3][0]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[1][2]=='O' || board[1][2]=='T')  && (board[0][3]=='O' || board[0][3]=='T') )
	levee=true;
	
	if(levee)
	{
		cout<<"O won"<<endl;
		continue;
	}
	
	levee=false;
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	if(board[i][j]=='.')
	{
		levee=true;
	}
	if(levee)
	{
		cout<<"Game has not completed"<<endl;
		continue;
	}
	
	cout<<"Draw"<<endl;
}	
	
	
}
