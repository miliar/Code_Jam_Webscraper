#include<iostream>
using namespace std;
#include<algorithm>
#include<cstdio>
#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
int main()
{
	int i,t,k,j;
	scanf("%d",&t);
	vector<int> v;
	char s[10];
	int a[10][10];
	int complete,win;
	for(k=1;k<=t;k++)
	{
		complete=1;
		win=1;
		v.clear();
		for(i=0;i<4;i++)
		{
			scanf("%s",s);
			for(j=0;j<4;j++)
			{
				if(s[j]=='.')
				{
					a[i][j]=-20;
					complete=0;
				}
				else if(s[j]=='X')
				{
					a[i][j]=1;
				}
				else if(s[j]=='O')
				{
					a[i][j]=-1;
				}
				else if(s[j]=='T')
				{
					a[i][j]=0;
				}
			}
		}
		int sum;
		for(i=0;i<4;i++)
		{
			sum=0;
			for(j=0;j<4;j++)
			{
				sum+=a[i][j];
			}
			v.push_back(sum);
			sum=0;
			for(j=0;j<4;j++)
			{
				sum+=a[j][i];
			}
			v.push_back(sum);
		}
		sum=0;
		for(j=0;j<4;j++) sum+=a[j][j];
		v.push_back(sum);
		sum=0;
		for(j=0;j<4;j++) sum+=a[3-j][j];
		v.push_back(sum);
		sort(v.begin(),v.end());
		printf("Case #%d: ",k);
		if(binary_search (v.begin(), v.end(), 4) or binary_search (v.begin(), v.end(), 3)) 
		{
			printf("X won\n");
		}
		else if(binary_search (v.begin(), v.end(), -3) or binary_search (v.begin(), v.end(), -4)) 
		{
			printf("O won\n");
		}
		else if(complete)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}
		getchar();
	}
	return 0;
}
