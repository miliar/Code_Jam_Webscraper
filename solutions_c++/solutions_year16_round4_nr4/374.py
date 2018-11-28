#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
using namespace std;
//r<p<s r=0,p=1,s=2
int mat[50][50];
int mm[50][50];
int n;
int seq[100];
bool dfs(int dc,int now)
{
	bool key=false;
	
	if(dc==n)return true;
	int c=seq[dc];
	for(int i=0;i<n;i++)
	{
		if(mm[c][i])
		if(((1<<i)&now)==0)
		{
			key=true;
			if(!dfs(dc+1,now+(1<<i)))return false;
		}
	}
	return key;
}
int jc[5]={1,1,2,6,24};
int main()
{
	int T,cas=0;
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)scanf("%1d",&mat[i][j]);
		int ans=9999;
		
		for(int i=0;i<n;i++)seq[i]=i;
		for(int i=0;i<(1<<(n*n));i++)
		{
			bool key=true;
			int cnt=0;
			for(int j=0;j<n;j++)
			{
				for(int l=0;l<n;l++)
				{
					int dd=j*n+l;
					if((1<<(dd))&i)mm[j][l]=1;
					else mm[j][l]=0;
					if(mat[j][l])
					{
						if((1<<(dd))&i);
						else key=false;
					}
					else if((1<<(dd))&i)cnt++;
				}
			}
			if(!key)continue;
			if(cnt>=ans)continue;
			bool kk=true;
			for(int j=0;j<jc[n];j++)
			{
				kk&=dfs(0,0);
				next_permutation(seq,seq+n);
			}
			if(kk){
				ans=cnt;
			}
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
}
/*
1
4
1111
1010
0001
1100
*/