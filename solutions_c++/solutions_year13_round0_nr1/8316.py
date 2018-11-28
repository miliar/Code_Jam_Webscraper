#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{
	int T,i,j,k,won,dot;
	ifstream fin("A-small-attempt1.in");
	ofstream fout("A-small-attempt1.out");
	
	fin>>T;
	
	char grid[4][5],ch;
	
	for(i=0;i<T;i++)
	{
		for(j=0;j<4;j++)
			fin>>grid[j];
			
		fout<<"Case #"<<i+1<<": ";
		
		won = 1;
		dot = 0;
		for(j=0;j<4;j++)
		{
			won = 1;
			ch = grid[j][0];
			if(ch == '.')
			{
				dot++;
				//break;
			}
			for(k=1;k<4;k++)
			{
				if(grid[j][k] == '.')
				{
					dot++;
					won = 0;
				}	
				else if(!(ch == grid[j][k] || grid[j][k] == 'T'))
				{
					won = 0;
					break;
				}
			}
			if(won)
			{
				fout<<ch<<" won"<<endl;
				break;
			}
		}
		if(won && dot != 16)
			continue;
		
		won = 1;
		for(j=0;j<4;j++)
		{
			won = 1;
			ch = grid[0][j];
			if(ch == '.')
			{
				if(j == 3)
					won = 0;
				else
					continue;
			}
			for(k=1;k<4;k++)
			{
				if(!(ch == grid[k][j] || grid[k][j] == 'T'))
				{
					won = 0;
					break;
				}
			}
			if(won)
			{
				fout<<ch<<" won"<<endl;
				break;
			}
		}
		if(won && dot != 16)
			continue;
		
		won = 1;
		ch = grid[0][0];
		if(ch != '.')
		{
			for(j=1;j<4;j++)
			{
				if(!(ch == grid[j][j] || grid[j][j] == 'T'))
				{
					won = 0;
					break;
				}
			}
			if(won)
			{
				fout<<ch<<" won"<<endl;
				continue;
			}
		}
		
		won = 1;
		ch = grid[0][3];
		if(ch != '.')
		{
			for(j=1;j<4;j++)
			{
				if(!(ch == grid[j][3-j] || grid[j][3-j] == 'T'))
				{
					won = 0;
					break;
				}
			}
			if(won)
			{
				fout<<ch<<" won"<<endl;
				continue;
			}
		}
		
		if(dot)
			fout<<"Game has not completed"<<endl;
		else
			fout<<"Draw"<<endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
