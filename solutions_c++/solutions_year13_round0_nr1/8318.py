#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;
bool checkForX(char a[4][4]);
bool checkFor0(char a[4][4]);
bool checkForG(char a[4][4]);

int main()
{
	int T,i=0,j=0,k=0;
	bool owin=false,xwin=false,draw=false,going=false;
	cin>>T;
	char puzz[4][4];
	for(i=0;i<T;i++)
	{
		owin=false,xwin=false,draw=false,going=false;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>puzz[j][k];
				//cout<<puzz[j][k]<<"  ";
			}
			//cout<<endl;
		}
		//cout<<endl;
		owin=checkFor0(puzz);
		xwin=checkForX(puzz);
		going=checkForG(puzz);
		if(owin && !xwin) cout<<"Case #"<<i+1<<": "<<"O won"<<endl;
		else if(xwin && !owin) cout<<"Case #"<<i+1<<": "<<"X won"<<endl;
		else if(going && !owin && !xwin) cout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
		else if(!xwin && !owin && !going) cout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
	}
return 0;
}

bool checkFor0(char a[4][4])
{
	for(int row=0;row<4;row++)
	{
		//cout<<"row "<<row+1<<"checked"<<endl;
		if(((a[row][0]=='O')||(a[row][0]=='T'))&&((a[row][1]=='O')||(a[row][1]=='T'))&&((a[row][2]=='O')||(a[row][2]=='T'))&&((a[row][3]=='O')||(a[row][3]=='T')))
		{
			//cout<<"true returning"<<endl;
			return true;
		}
	}
	for(int col=0;col<4;col++)
	{//cout<<"col "<<col+1<<"checked"<<endl;
		if(((a[0][col]=='O')||(a[0][col]=='T'))&&((a[1][col]=='O')||(a[1][col]=='T'))&&((a[2][col]=='O')||(a[2][col]=='T'))&&((a[3][col]=='O')||(a[3][col]=='T')))
		{
			return true;
		}
	}
	if(((a[0][0]=='O')||(a[0][0]=='T'))&&((a[1][1]=='O')||(a[1][1]=='T'))&&((a[2][2]=='O')||(a[2][2]=='T'))&&((a[3][3]=='O')||(a[3][3]=='T')))
	{
		return true;
	}
	if(((a[0][3]=='O')||(a[0][3]=='T'))&&((a[1][2]=='O')||(a[1][2]=='T'))&&((a[2][1]=='O')||(a[2][1]=='T'))&&((a[3][0]=='O')||(a[3][0]=='T')))
	{
		return true;
	}
return false;
}


bool checkForX(char a[4][4])
{
	for(int row=0;row<4;row++)
	{
		if(((a[row][0]=='X')||(a[row][0]=='T'))&&((a[row][1]=='X')||(a[row][1]=='T'))&&((a[row][2]=='X')||(a[row][2]=='T'))&&((a[row][3]=='X')||(a[row][3]=='T')))
		{
			return true;
		}
	}
	for(int col=0;col<4;col++)
	{
		if(((a[0][col]=='X')||(a[0][col]=='T'))&&((a[1][col]=='X')||(a[1][col]=='T'))&&((a[2][col]=='X')||(a[2][col]=='T'))&&((a[3][col]=='X')||(a[3][col]=='T')))
		{
			return true;
		}
	}
	if(((a[0][0]=='X')||(a[0][0]=='X'))&&((a[1][1]=='X')||(a[1][1]=='T'))&&((a[2][2]=='X')||(a[2][2]=='T'))&&((a[3][3]=='X')||(a[3][3]=='T')))
	{
		return true;
	}
	if(((a[0][3]=='X')||(a[0][3]=='T'))&&((a[1][2]=='X')||(a[1][2]=='T'))&&((a[2][1]=='X')||(a[2][1]=='T'))&&((a[3][0]=='X')||(a[3][0]=='T')))
	{
		return true;
	}
return false;
}


bool checkForG(char a[4][4])
{
	for(int row=0;row<4;row++)
	{
		if(((a[row][0]=='.')||(a[row][0]=='T'))&&((a[row][1]=='.')||(a[row][1]=='T'))&&((a[row][2]=='.')||(a[row][2]=='T'))&&((a[row][3]=='.')||(a[row][3]=='T')))
		{
			return true;
		}
	}
	for(int col=0;col<4;col++)
	{
		if(((a[0][col]=='.')||(a[0][col]=='T'))&&((a[1][col]=='.')||(a[1][col]=='T'))&&((a[2][col]=='.')||(a[2][col]=='T'))&&((a[3][col]=='.')||(a[3][col]=='T')))
		{
			return true;
		}
	}
	if(((a[0][0]=='.')||(a[0][0]=='T'))&&((a[1][1]=='.')||(a[1][1]=='T'))&&((a[2][2]=='.')||(a[2][2]=='T'))&&((a[3][3]=='.')||(a[3][3]=='T')))
	{
		return true;
	}
	if(((a[0][3]=='.')||(a[0][3]=='T'))&&((a[1][2]=='.')||(a[1][2]=='T'))&&((a[2][1]=='.')||(a[2][1]=='T'))&&((a[3][0]=='.')||(a[3][0]=='T')))
	{
		return true;
	}
return false;
}

