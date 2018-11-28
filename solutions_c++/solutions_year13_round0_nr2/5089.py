#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string.h>
using namespace std;
int lawn[101][101] = {};
bool deleteRow[101], deleteCol[101];		//recode the line and column that has been deleted 
int M,N;

bool isIn(int i,int j)
{
	return ((!deleteRow[i])&&(!deleteCol[j]));			//i is not delete and j is not delete
}

bool lawnEmpty()
{
	int i,j;
	for(i = 0;i<N;i++)
	{
		if(deleteRow[i]==false){break;}
	}
	if(i==N){return true;}
	for(j = 0;j<M;j++)
	{
		if(deleteCol[j]==false){break;}
	}
	if(j==M){return true;}
	return false;
}

bool deleteLine(int i,int j)
{
	bool del = false;
	//judge row
	int col,row;
	for(col = 0; col < M; col++)
	{
		if(isIn(i,col))
		{
			if(lawn[i][j]!=lawn[i][col])
			{
				break;
			}
		}
	}
	if(col==M){deleteRow[i]=true;del=true;}
	//judge col
	for(row = 0; row < N; row++)
	{
		if(isIn(row,j))
		{
			if(lawn[i][j]!=lawn[row][j])
			{
				break;
			}
		}
	}
	if(row==N){deleteCol[j]=true;del=true;}
	return del;
}

int main()
{
	int caseNum = 1;
	FILE *input, *output;
	if((input = fopen("test","r"))==NULL)
	{
		printf("can't open file\n");
		exit(0);
	}
	output = fopen("output","w");
	char temp;
	int T;
	fscanf(input,"%d%c",&T,&temp);
	while(T--)
	{
		memset(lawn,0,sizeof(lawn));
		fscanf(input,"%d %d%c",&N,&M,&temp);
		memset(deleteRow,false,sizeof(deleteRow));
		memset(deleteCol,false,sizeof(deleteCol));
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				fscanf(input,"%d",&lawn[i][j]);
			}
		}
		//algorithm goes
		while(true)
		{
			//find minimum
			int minh = 1000,mini,minj;
			bool noDel = true;
			int i,j;
			for(i=0;i<N;i++)
			{
				for(j=0;j<M;j++)
				{
					if(isIn(i,j)&&lawn[i][j]<minh)
					{
						noDel = false;				//nothing is in the lawn(empty)
						minh = lawn[i][j];
						mini = i;minj = j;
					}
				}
			}
			if(noDel){break;}
			if(!deleteLine(mini,minj)){break;}		//no delete operation happens
		}
		if(lawnEmpty())
		{
			fprintf(output,"Case #%d: YES\n",caseNum++);
		}
		else
		{
			fprintf(output,"Case #%d: NO\n",caseNum++);
		}
	}
	system("pause");
	return 0;
}