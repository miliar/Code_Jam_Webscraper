#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
using namespace std;
typedef pair<int,int>pii;
int dp[101][2201];
int main()
{
	FILE *fr=fopen("b-large.in","r");
	FILE *fw=fopen("out1.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=0;p<data;p++)
	{
		int att,ene,num;
		fscanf(fr,"%d%d%d",&att,&ene,&num);
		vector<pii>vec;
		for(int i=0;i<num;i++)
		{
			int za,zb;
			fscanf(fr,"%d%d",&za,&zb);
			vec.push_back(make_pair(za,zb));
		}
		vector<int>kai;
		vector<int>k2;
		for(int i=0;i<num;i++)
		{
			for(int j=10;j>=0;j--)
			{
				if(vec[i].first-j*ene>0)
				{
					kai.push_back(((vec[i].first-j*ene)+att-1)/att);
					k2.push_back(j);
					//printf("%d\n",kai[i]);
					break;
				}
			}
		}
		for(int i=0;i<=num;i++)
		{
			for(int j=0;j<=num*11;j++)
			{
				dp[i][j]=-2100000000;
			}
		}
		dp[0][1]=0;
		for(int i=0;i<num;i++)
		{
			for(int j=0;j<=num*11;j++)
			{
				dp[i+1][j+(vec[i].first+ene-1)/ene]=max(dp[i+1][j+(vec[i].first+ene-1)/ene],dp[i][j]);
				if(j-kai[i]+k2[i]>=0)
				{
					dp[i+1][j-kai[i]+k2[i]]=max(dp[i+1][j-kai[i]+k2[i]],dp[i][j]+vec[i].second);
				}
				//if(j<=4)printf("%11d %11d   ",dp[i][j][0],dp[i][j][1]);
			}
			//printf("\n");
		}
		int maxi=0;
		for(int i=0;i<=num*11;i++)
		{
			maxi=max(maxi,dp[num][i]);
		}
		fprintf(fw,"Case #%d: %d\n",p+1,maxi);
	}
}