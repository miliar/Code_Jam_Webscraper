#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<numeric>

using namespace std;

int main()
{
	int n, t;
	char tt[4][5];
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		cin>>tt[0]>>tt[1]>>tt[2]>>tt[3];
		int g=1; 
		char k='k';
		for(int i=0;i<4 && k=='k';i++)
		{
			int f=1;
			for(int j=0;j<4;j++)
			{
				if(tt[i][j] == 'X' || tt[i][j] == '.')
				{
					f=0;
					if(tt[i][j] == '.')
					{
						g=0;
					}
				}
			}
			if(f==1)
			{
				k = 'o';
				break;
			}
		}
		for(int j=0;j<4 && k=='k';j++)
		{
			int f=1;
			for(int i=0;i<4;i++)
			{
				if(tt[i][j] == 'X' || tt[i][j] == '.')
				{
					f=0;
				}
			}
			if(f==1)
			{
				k = 'o';
				break;
			}
		}
		
		if(k=='k')
		{
			int f = 1;
			for(int i=0;i<4;i++)
			{
				if(tt[i][i] == 'X' || tt[i][i] == '.')
				{
					f=0;
				}
			}
			if(f==1)
			{
				k = 'o';
				//break;
			}
		}
		
		if(k=='k')
		{
			int f = 1;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4 ;j++)
				{
					if(i+j==3 && (tt[i][j] == 'X' || tt[i][j] == '.'))
					{
						f=0;
					}
					
				}
			}
			if(f==1)
			{
				k = 'o';
				
			}
		}
		
		for(int i=0;i<4 && k=='k';i++)
		{
			int f=1;
			for(int j=0;j<4;j++)
			{
				if(tt[i][j] == 'O' || tt[i][j] == '.')
				{
					f=0;
					
				}
			}
			if(f==1)
			{
				k = 'x';
				break;
			}
		}
		
		for(int j=0;j<4 && k=='k';j++)
		{
			int f=1;
			for(int i=0;i<4;i++)
			{
				if(tt[i][j] == 'O' || tt[i][j] == '.')
				{
					f=0;
				}
			}
			if(f==1)
			{
				k = 'x';
				break;
			}
		}
		
		if(k=='k')
		{
			int f = 1;
			for(int i=0;i<4;i++)
			{
				if(tt[i][i] == 'O' || tt[i][i] == '.')
				{
					f=0;
				}
			}
			if(f==1)
			{
				k = 'x';
				//break;
			}
		}
		
		if(k=='k')
		{
			int f = 1;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4 ;j++)
				{
					if(i+j==3 && (tt[i][j] == 'O' || tt[i][j] == '.'))
					{
						f=0;
					}
					
				}
			}
			if(f==1)
			{
				k = 'x';
				
			}
		}
		
		if(k=='k')
		{
			if(g==1)
			{
				cout<<"Case #"<<p<<": Draw"<<endl;
			}
			else
			{
				cout<<"Case #"<<p<<": Game has not completed"<<endl;
			}
		}
		else if(k=='o')
		{
			cout<<"Case #"<<p<<": O won"<<endl;
		}
		else if(k=='x')
		{
			cout<<"Case #"<<p<<": X won"<<endl;
		}
	}
	return 0;
}
