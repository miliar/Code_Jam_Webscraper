#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

#define TRUE 1
#define FALSE 0
#define SIZE 10

int rect[SIZE][SIZE];
int rows,cols;

bool check()
{
	int rowmin[SIZE],colmin[SIZE];
	bool flag[SIZE][SIZE];
	for(int i=0;i<SIZE;i++) 
	{
		rowmin[i] = 101;
		colmin[i] = 101;
	}
	for(int i=0;i<rows;i++)
	{
		for(int j=0;j<cols;j++)
		{
			rowmin[i] = min(rowmin[i],rect[i][j]);
			colmin[j] = min(colmin[j],rect[i][j]);
			flag[i][j] = 0;
		}
	}
	for(int i=0;i<rows;i++)
		for(int j=0;j<cols;j++)
		{
			int k=0;
			if(rect[i][j]==rowmin[i])
			for(k=0;k<rows;k++)
				if(rect[k][j]!=rect[i][j]) break;
			if(k!=rows && rect[i][j]==colmin[j])
			{
				for(k=0;k<cols;k++)
					if(rect[i][k]!=rect[i][j]) break;
				if(k!=cols) return FALSE;
			}
		}
	return TRUE;
}

int main()
{
    freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int cases,val;
	string rowvals;
	cin>>cases;
	for(int t=1;t<=cases;t++)
	{
		cin>>rows>>cols;
		for(int i=0;i<rows;i++)
			for(int j=0;j<cols;j++)
			{
				scanf("%d",&val);
				rect[i][j] = val;
			}
		if(rows==1 || cols==1 || check())
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);
	}
	return 0;
}

