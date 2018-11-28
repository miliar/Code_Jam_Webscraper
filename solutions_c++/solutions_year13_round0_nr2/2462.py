#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
#define SIZE 100
using namespace std;
int board[SIZE+1][SIZE+1],score[SIZE+1][SIZE+1];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.txt","w",stdout);
	int cases,t,i,j,k,row,column,large,index[2];
	bool check,cut;
	cin>>t;
	for(cases=1;cases<=t;cases++)
	{
		cin>>row>>column;
		check=true;
		for(i=0;i<row;i++)
			for(j=0;j<column;j++)
			{
				cin>>board[i][j];
				score[i][j]=100;
				if(board[i][j]!=100)
					check=false;
			}
		if(check)
		{
			printf("Case #%d: YES\n",cases);
			continue;
		}
		while(true)
		{
			check=true;
			large=0;
			for(i=0;i<row;i++)
				for(j=0;j<column;j++)
					if(board[i][j]!=score[i][j])
					{
						check=false;
						if(board[i][j]>large)
						{
							index[0]=i, index[1]=j;
							large=board[i][j];
						}
					}
			if(check)
				break;
			cut=true;
			for(k=0;k<row;k++)
				if(board[k][index[1]] == 100 || board[k][index[1]] > large)
					break;
			if(k==row)
			{
				cut=false;
				for(k=0;k<row;k++)
					score[k][index[1]]=large;
			}
			//no cut
			else
			{
				for(k=0;k<column;k++)
					if(board[index[0]][k] == 100 || board[index[0]][k] > large)
						break;
				if(k==column)
				{
					cut=false;
					for(k=0;k<column;k++)
						score[index[0]][k]=large;
				}
			}
			//no cut
			if(cut)
				break;
		}
		if(!check && cut)
			printf("Case #%d: NO\n",cases);
		else
			printf("Case #%d: YES\n",cases);
	}
	return 0;
}
