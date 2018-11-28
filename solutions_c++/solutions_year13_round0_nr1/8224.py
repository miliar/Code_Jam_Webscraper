#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <fstream>
using namespace std;

char box[4][4];

int check()
{

	int tx,ty;
	
	//finding pos of t
	
	
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(box[i][j]=='T')
			{
				tx=i;
				ty=j;
			}
		}
	}			
	
	//checking equal rows/columns
	
	
	for(int i=0;i<4;i++)
	{
		if((box[i][0]==box[i][1])&&(box[i][1]==box[i][2])&&(box[i][2]==box[i][3]))
		{
			if(box[i][0]=='X')
			{
				return 1;
			}
			if(box[i][0]=='O')
			{
				return 2;
			}
		}
		if((box[0][i]==box[1][i])&&(box[1][i]==box[2][i])&&(box[2][i]==box[3][i]))
		{
			if(box[0][i]=='X')
			{
				return 1;
			}
			if(box[0][i]=='O')
			{
				return 2;
			}
		}
	}

	//checking equal diagonals
	
	
	if((box[0][0]==box[1][1])&&(box[1][1]==box[2][2])&&(box[2][2]==box[3][3]))
	{
			if(box[0][0]=='X')
			{
				return 1;
			}
			if(box[0][0]=='O')
			{
				return 2;
			}
	}
	if((box[0][3]==box[1][2])&&(box[1][2]==box[2][1])&&(box[2][1]==box[3][0]))
	{
			if(box[0][3]=='X')
			{
				return 1;
			}
			if(box[0][3]=='O')
			{
				return 2;
			}
	}

	//checking tx and ty
	
	char TX[3],TY[3],m=0,n=0;
	for(int i=0;i<4;i++)
	{
		
		if(i==ty)
		{
			continue;
		}
		else
		{
			TX[m]=box[tx][i];
			m++;
		}
	}

	if((TX[0]==TX[1])&&(TX[1]==TX[2]))
	{
			if(TX[0]=='X')
			{
				return 1;
			}
			if(TX[0]=='O')
			{
				return 2;
			}
	}
	for(int i=0;i<4;i++)
	{
		
		if(i==tx)
		{
			continue;
		}
		else
		{
			TY[n]=box[i][ty];
			n++;
		}
	}

	if((TY[0]==TY[1])&&(TY[1]==TY[2]))
	{
			if(TY[0]=='X')
			{
				return 1;
			}
			if(TY[0]=='O')
			{
				return 2;
			}
	}

	//checking td
	
	
	char TD[3],l=0,p=3;;
	if(tx==ty)
	{
		for(int i=0;i<4;i++)
		{
		
			if(i==tx)
			{
				continue;
			}
			else
			{
				TD[l]=box[i][i];
				l++;
			}
		}
	}
	if((tx==3&&ty==0)||(tx==2&&ty==1)||(tx==1&&ty==2)||(tx==0&&ty==3))
	{
		for(int i=0;i<4;i++)
		{
		
			if(i==tx)
			{
				p--;
				continue;
			}
			else
			{
				TD[l]=box[i][p];
				l++;
				p--;
			}
		}
	}

	if((TD[0]==TD[1])&&(TD[1]==TD[2]))
	{
			
			if(TD[0]=='X')
			{
				
				return 1;
			}
			if(TD[0]=='O')
			{
				
				return 2;
			}
	}
	for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(box[i][j]=='.')
				{
					return -1;
				}
			}	
		}
	return 0;	
}

int main()
{
	
	//file input
	int t,z=1;
	ifstream fin;
	fin.open("A-small-attempt1.in",ios::in);
	ofstream fout;
	fout.open("output.txt",ios::out);
	fin>>t;
	
	char ch;
	int x=0,y=0;
		while(!fin.eof())
		{
				
			fin>>box[x][y];
			
			y++;
			if(y==4)
			{
				y=0;
				x++;
				if(x==4)
				{
					int r=check();
					fout<<"Case #"<<z<<": ";
					if(r==-1)
					{
						fout<<"Game has not completed";
					}
					if(r==0)
					{
						fout<<"Draw";
					}
					if(r==1)
					{
						fout<<"X won";
					}
					if(r==2)
					{
						fout<<"O won";
					}
					
					fout<<"\n";
				
					x=0;
					z++;
				}	
			}		
		}
	fin.close();
	fout.close();
	cout<<"\nPress any key to EXIT..";
	getch();
	return 0;
}
