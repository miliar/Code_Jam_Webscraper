/*
Problem :Deciteful war
contest : Google code jam
author : saurabh jain
date :12/4/2014
*/

#include<iostream>
#include<stdio.h>
#include<string.h>
#include<iterator>
#include<stdlib.h>
#include<map>
#include<vector>
#include<algorithm>
#define MOD 1000000007
#define max(x,y)((x>y)?x:y)
#define min(x,y)((x<y)>x:y)
#define FEP(i,a,b) for(int i=a;i<b;i++)
#define PI 3.14
using namespace std;
int main(int argc, char* argv[])
{	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		int n;
		scanf("%d",&n);
		double naomi[n],ken[n];
		FEP(i,0,n)
			cin>>naomi[i];
		FEP(i,0,n)
			cin>>ken[i];
			
		if(n==1)
		{
			if(naomi[0]>ken[0])
				printf("Case #%d: %d %d\n",k,1,1);
			else
				printf("Case #%d: %d %d\n",k,0,0);
			continue;
		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		//for optimal WAR
		int j=0;
		int optimal=n;
		FEP(i,0,n)
		{	
			if(ken[i]>naomi[j])
			{
				optimal--;
				j++;
			}
		}
		
		int deciteful=0;
		j=n-1;
		for(int i=n-1;i>=0;i--)
		{	
			if(naomi[j]>ken[i])
			{
				deciteful++;
				j--;
			}
		}
		printf("Case #%d: %d %d\n",k,deciteful,optimal);
	}	
}
