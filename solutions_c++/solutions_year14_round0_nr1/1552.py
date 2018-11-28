//============================================================================
// Name        : a1.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<iostream>
#define N 100050
#define LL __int64
using namespace std;
int a[22][22],b[22][22];
int bo[22];
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,i,j,k,ri=0,n,m;
	scanf("%d",&tt);
	while(tt--)
	{
		ri++;
		memset(bo,0,sizeof(bo));
		scanf("%d",&n);
		for(i=1;i<5;i++)
			for(j=1;j<5;j++)
			{
				scanf("%d",&a[i][j]);
				if(i==n)
				{
					bo[a[i][j]]++;
				}
			}
		scanf("%d",&m);
		for(i=1;i<5;i++)
		{
			for(j=1;j<5;j++)
			{
				scanf("%d",&b[i][j]);
				if(i==m)
				{
					bo[b[i][j]]++;
				}
			}
		}
		int cnt=0,pos=-1;
		for(i=1;i<=16;i++)
		{
			if(bo[i]==2){
				pos=i;
				cnt++;
			}
		}
		if(cnt==0)printf("Case #%d: Volunteer cheated!\n",ri);
		else if(cnt==1)printf("Case #%d: %d\n",ri,pos);
		else printf("Case #%d: Bad magician!\n",ri);
	}
}
