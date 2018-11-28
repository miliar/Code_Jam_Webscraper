#include<iostream>
#include<vector>
#include<stdio.h>
#include<string>
#include<string.h>
using namespace std;


int main ()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	char g[4][4];
	int n,temp,dots,sum,counter=1;
	cin>>n;
	cin.ignore();
	while(n--)
	{
		int rows[4]={0},coloumns[4]={0};
		dots=0;
		for(int i=0;i<4;i++)
		{
			temp=0;
			for(int j=0;j<4;j++)
			{
				cin>>g[i][j];
				if(g[i][j]=='.')
				{
					temp=10;
					dots++;
				}
				if(g[i][j]=='X')
					temp=1;
				if(g[i][j]=='O')
					temp=-1;
				rows[i]+=temp;
				coloumns[j]+=temp;
			}
		}
		sum=0;
		temp=0;
		for(int i=0;i<4;i++)
		{
			if(g[i][i]=='.')
			{
				temp=10;
				dots++;
			}
			if(g[i][i]=='X')
				temp=1;
			if(g[i][i]=='O')
				temp=-1;
			sum+=temp;
		}
		if(sum==3||sum==4)
		{
			printf("Case #%d: X won\n",counter++);
			continue;
		}
		if(sum==-3||sum==-4)
		{
			printf("Case #%d: O won\n",counter++);
			continue;
		}
		sum=0;
		temp=0;
		for(int i=0,j=3;i<4;i++,j--)
		{
			if(g[i][j]=='.')
			{
				temp=10;
				dots++;
			}
			if(g[i][j]=='X')
				temp=1;
			if(g[i][j]=='O')
				temp=-1;
			sum+=temp;
		}
		if(sum==3||sum==4)
		{
			printf("Case #%d: X won\n",counter++);
			continue;
		}
		if(sum==-3||sum==-4)
		{
			printf("Case #%d: O won\n",counter++);
			continue;
		}
		temp=0;
		for(int i=0;i<4;i++)
		{
			if(rows[i]==3 || rows[i]==4 || coloumns[i]==3 || coloumns[i]==4)
			{
				temp=1;
				break;
			}
			if(rows[i]==-3 || rows[i]==-4 || coloumns[i]==-3 || coloumns[i]==-4)
			{
				temp=-1;
				break;
			}
		}
		if(temp==1)
			printf("Case #%d: X won\n",counter++);
		else if(temp==-1)
			printf("Case #%d: O won\n",counter++);
		else if(dots)
			printf("Case #%d: Game has not completed\n",counter++);
		else
			printf("Case #%d: Draw\n",counter++);
	}
}