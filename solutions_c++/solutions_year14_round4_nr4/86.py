//count the number of MST!! I cannot code...

#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
vector<string>vec;
int map[8][8];
int calc(vector<int>v)
{
	if(v.empty())
	{
		return 0;
	}
	int ret=vec[v[0]].size()+1;
	for(int i=1;i<v.size();i++)
	{
		int maxi=0;
		for(int j=0;j<i;j++)
		{
			maxi=max(maxi,map[v[i]][v[j]]);
		}
		ret+=vec[v[i]].size()-maxi;
	}
	return ret;
}
int main()
{
	FILE *fr=fopen("d-small-attempt0.in","r");
	FILE *fw=fopen("out.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=0;p<data;p++)
	{
		vec.clear();
		int num,div;
		fscanf(fr,"%d%d",&num,&div);
		char gomi;
		fscanf(fr,"%c",&gomi);
		for(int i=0;i<num;i++)
		{
			string str;
			for(;;)
			{
				char zan;
				fscanf(fr,"%c",&zan);
				if(zan=='\n')
				{
					break;
				}
				str.push_back(zan);
			}
			vec.push_back(str);
		}
		for(int i=0;i<num;i++)
		{
			for(int j=0;j<num;j++)
			{
				int now=0;
				for(int k=0;k<min(vec[i].size(),vec[j].size());k++)
				{
					if(vec[i][k]==vec[j][k])
					{
						now++;
					}
					else
					{
						break;
					}
				}
				map[i][j]=now;
				//printf("%d ",map[i][j]);
			}//printf("\n");
		}
		int exm=1;
		for(int i=0;i<num;i++)
		{
			exm*=div;
		}
		int maxi=0;
		int n=0;
		for(int i=0;i<exm;i++)
		{
			int now=i;
			vector<int>v[4];
			for(int j=0;j<num;j++)
			{
				v[now%div].push_back(j);
				now/=div;
			}
			int sum=0;
			for(int i=0;i<div;i++)
			{
				sum+=calc(v[i]);
			}
			if(maxi<sum)
			{
				maxi=sum;
				n=1;
			}
			else
			{
				if(maxi==sum)
				{
					n++;
				}
			}
		}
		fprintf(fw,"Case #%d: %d %d\n",p+1,maxi,n);
	}
}