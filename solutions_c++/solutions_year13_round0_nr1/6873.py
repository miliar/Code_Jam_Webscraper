#include<iostream>
#include<fstream>
using namespace std;
void main()
{
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("A-large.out");
	int t;
	in>>t;
	for(int i=1;i<=t;i++)
	{
		int r=-1,c=-1;
		char arr[4][4];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				in>>arr[j][k];
				if(arr[j][k]=='T')
				{
					r=j;
					c=k;
				}
			}
		}
		out<<"Case #"<<i<<": ";
		int x=0;
		int o=0;
		int count=0;
		if(r!=-1)
		{
		for(int j=0;j<4;j++)
		{
			arr[r][c]='X';
			if(arr[j][0]=='X' && arr[j][1]=='X' && arr[j][2]=='X' && arr[j][3]=='X')
			{
				x++;
				count++;
			}
			arr[r][c]='O';
			if(arr[j][0]=='O' && arr[j][1]=='O' && arr[j][2]=='O' && arr[j][3]=='O')
			{
				o++;
				count++;
			}
			arr[r][c]='T';
		}
		for(int j=0;j<4;j++)
		{
			arr[r][c]='X';
			if(arr[0][j]=='X' && arr[1][j]=='X' && arr[2][j]=='X' && arr[3][j]=='X')
			{
				x++;
				count++;
			}
			arr[r][c]='O';
			if(arr[0][j]=='O' && arr[1][j]=='O' && arr[2][j]=='O' && arr[3][j]=='O')
			{
				o++;
				count++;
			}
			arr[r][c]='T';
		}
		arr[r][c]='X';
		if(arr[0][0]=='X' && arr[1][1]=='X' && arr[2][2]=='X' && arr[3][3]=='X')
		{
			x++;
			count++;
		}
		arr[r][c]='O';
		if(arr[0][0]=='O' && arr[1][1]=='O' && arr[2][2]=='O' && arr[3][3]=='O')
		{
			o++;
			count++;
		}
		arr[r][c]='X';
		if(arr[0][3]=='X' && arr[1][2]=='X' && arr[2][1]=='X' && arr[3][0]=='X')
		{
			x++;
			count++;
		}
		arr[r][c]='O';
		if(arr[0][3]=='O' && arr[1][2]=='O' && arr[2][1]=='O' && arr[3][0]=='O')
		{
			o++;
			count++;
		}
		arr[r][c]='T';
		}
		else
		{
		for(int j=0;j<4;j++)
		{
			if(arr[j][0]=='X' && arr[j][1]=='X' && arr[j][2]=='X' && arr[j][3]=='X')
			{
				x++;
				count++;
			}
			if(arr[j][0]=='O' && arr[j][1]=='O' && arr[j][2]=='O' && arr[j][3]=='O')
			{
				o++;
				count++;
			}
		}
		for(int j=0;j<4;j++)
		{
			if(arr[0][j]=='X' && arr[1][j]=='X' && arr[2][j]=='X' && arr[3][j]=='X')
			{
				x++;
				count++;
			}
			if(arr[0][j]=='O' && arr[1][j]=='O' && arr[2][j]=='O' && arr[3][j]=='O')
			{
				o++;
				count++;
			}
		}
		if(arr[0][0]=='X' && arr[1][1]=='X' && arr[2][2]=='X' && arr[3][3]=='X')
		{
			x++;
			count++;
		}
		if(arr[0][0]=='O' && arr[1][1]=='O' && arr[2][2]=='O' && arr[3][3]=='O')
		{
			o++;
			count++;
		}
		if(arr[0][3]=='X' && arr[1][2]=='X' && arr[2][1]=='X' && arr[3][0]=='X')
		{
			x++;
			count++;
		}
		if(arr[0][3]=='O' && arr[1][2]=='O' && arr[2][1]=='O' && arr[3][0]=='O')
		{
			o++;
			count++;
		}
		}
		if(x!=0)
			out<<"X won";
		if(o!=0)
			out<<"O won";
		int p=0;
		if(count==0)
		{
			for(int j=0;j<4;j++)
			{
				for(int k=0;k<4;k++)
				{
					if(arr[j][k]=='.')
					{
						p++;
					}
				}
			}
		}
		if(p==0 && count==0)
			out<<"Draw";
		if(p!=0 && count==0)
			out<<"Game has not completed";
		out<<endl;
		in;
	}
}