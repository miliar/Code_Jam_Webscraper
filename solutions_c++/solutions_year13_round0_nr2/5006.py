#include "StdAfx.h"

#include <iostream>
#include <stdio.h>
using namespace std;
int N,M;
int g[105][105]; 
int hang[105],lie[105];
void fun(int t[105][105])
{
	int i,j;
	memset(hang,false,sizeof(hang)); 
	memset(lie,false,sizeof(lie)); 
	for(i=1;i<=N;i++)
	{
		int flag=0;
		for(j=1;j<=M;j++)
		{
			if(t[i][j]==0) {flag=1;break;} 
		} 
		if(flag==0) hang[i]=true; 
	} 
	for(j=1;j<=M;j++)
	{
		int flag=0;
		for(i=1;i<=N;i++)
		{
			if(t[i][j]==0) {flag=1;break;} 
		} 
		if(flag==0) lie[j]=true; 
	} 
} 
int main()
{
	freopen("B-small-attempt4.txt","r",stdin);freopen("B-small-attempt4out.txt","w",stdout);
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		cas++;
		int i,j;
		printf("Case #%d: ",cas);
		cin>>N>>M;
		int MAX=0; 
		for(i=1;i<=N;i++)
		{
			for(j=1;j<=M;j++)
			{
				cin>>g[i][j]; 
				if(g[i][j]>MAX) MAX=g[i][j]; 
			} 
		}
		int h,ttt=0; 
		for(h=1;h<MAX;h++)
		{
			int temp[105][105];
			memset(temp,0,sizeof(temp));
			for(i=1;i<=N;i++)
			{
				for(j=1;j<=M;j++)
				{
					if(g[i][j]==h) temp[i][j]=1; 
				} 
			}
			fun(temp);
			for(i=1;i<=N;i++)
			{
				if(hang[i]==false) continue;
				for(j=1;j<=M;j++) temp[i][j]=0; 
			} 
			for(j=1;j<=M;j++)
			{
				if(lie[j]==false) continue;
				for(i=1;i<=N;i++) temp[i][j]=0; 
			} 
			int cnt=0;
			for(i=1;i<=N;i++)
			{
				for(j=1;j<=M;j++)
				{
					if(temp[i][j]==1) cnt++; 
				}
			} 
			if(cnt>0) ttt=1; 
		}
		if(ttt==1) printf("NO\n");
		else printf("YES\n"); 
	}
	return 0;
} 