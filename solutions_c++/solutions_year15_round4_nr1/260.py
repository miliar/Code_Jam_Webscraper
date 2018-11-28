#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
using namespace std;
int map[102][102];
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int main()
{
	FILE *fr=fopen("A-large.in","r");
	FILE *fw=fopen("outl.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=1;p<=data;p++)
	{
		int mx,my;
		fscanf(fr,"%d%d",&mx,&my);
		for(int i=0;i<102;i++)for(int j=0;j<102;j++)map[i][j]=-2;
		for(int i=1;i<=mx;i++)
		{
			for(int j=1;j<=my;j++)
			{
				char zan;
				fscanf(fr," %c",&zan);
				if(zan=='.')map[i][j]=-1;
				if(zan=='v')map[i][j]=0;
				if(zan=='>')map[i][j]=1;
				if(zan=='^')map[i][j]=2;
				if(zan=='<')map[i][j]=3;
			}
		}
		fprintf(fw,"Case #%d: ",p);
		int cnt=0;
		for(int i=1;i<=mx;i++)
		{
			for(int j=1;j<=my;j++)
			{
				if(map[i][j]==-1)continue;
				int dat[4];
				for(int k=0;k<4;k++)
				{
					int nx=i,ny=j;
					dat[k]=0;
					for(;;)
					{
						if(map[nx][ny]==-2)
						{
							dat[k]=1;
							break;
						}
						nx+=dx[k];
						ny+=dy[k];
						if(map[nx][ny]!=-1&&map[nx][ny]!=-2)break;
					}
				}
				if(dat[0]+dat[1]+dat[2]+dat[3]==4)
				{
					fprintf(fw,"IMPOSSIBLE\n");
					goto l01;
				}
				if(dat[map[i][j]]==1)cnt++;
			}
		}
		fprintf(fw,"%d\n",cnt);
l01:;
	}
}