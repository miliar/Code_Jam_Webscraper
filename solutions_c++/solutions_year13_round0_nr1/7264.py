#include<iostream>
#include<stdio.h>

using namespace std;

char grid[4][5];

int row(int i)
{
	if(grid[i][0]=='.')
		return 0;
	int x,start=1;
	if(grid[i][0]=='T')
	{
		if(grid[i][1]=='.')
			return 0;
		x = grid[i][1] - 'A';
		start =2;
	}
	else
		x = grid[i][0]-'A';
	for(int j=start;j<4;j++)
	{
		if(grid[i][j]=='.')
			return 0;
		if((grid[i][j]-'A')!=x && grid[i][j]!='T')
			x = 1;
	}
	return x;
}

int col(int j)
{
	if(grid[0][j]=='.')
		return 0;
	int x,start=1;
	if(grid[0][j]=='T')
	{
		if(grid[1][j]=='.')
			return 0;
		x = grid[1][j] - 'A';
		start =2;
	}
	else
		x = grid[0][j]-'A';
	for(int i=start;i<4;i++)
	{
		if(grid[i][j]=='.')
			return 0;
		if((grid[i][j]-'A')!=x && grid[i][j]!='T')
			x = 1;
	}
	return x;
}

int getk(int k, int y)
{
	if(y==1)
		return k;
	return 3-k;
}

int diag(int y)
{
	int k = 0;
	if(grid[k][getk(k,y)]=='.')
		return 0;
	int x;
	if(grid[k][getk(k,y)]=='T')
	{
		k++;
		if(grid[k][getk(k,y)]=='.')
			return 0;
		x = grid[k][getk(k,y)] - 'A';
	}
	else
		x = grid[k][getk(k,y)]-'A';
	for(k++;k<4;k++)
	{
		if(grid[k][getk(k,y)]=='.')
			return 0;
		if((grid[k][getk(k,y)]-'A')!=x && grid[k][getk(k,y)]!='T')
			x = 1;
	}
	return x;	
}

int main()
{
	int t,k,i,j,x,comp;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		for(i=0;i<4;i++)
			scanf("%s",grid[i]);
		comp = 1;
		for(i=0;i<4;i++)		
		{
			x = row(i);
			comp = comp & x;
			if(x>1)
				break;
		}
		if(x<=1)
		{
			for(j=0;j<4;j++)
			{
				x = col(j);
				if(x>1)
					break;
			}
			if(x<=1)
			{
				x = diag(1);
				if(x<=1)
					x = diag(2);
			}
		}
		printf("Case #%d: ",k);
		if(x>1)
			printf("%c won\n",'A'+x);
		else if(comp==0)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}