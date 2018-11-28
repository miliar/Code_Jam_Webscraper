/*************************************************************************
    > File Name: c.cpp
    > Author: withwind
    > Mail: withwind93@gmail.com 
    > Created Time: 2013/4/13 10:11:05
 ************************************************************************/
#include <limits.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
using namespace std;
#define llg long long
llg p[10000000],pn=0;
llg pp[10000],ppn=0;
int vis[10000010];
int pali(llg n)
{
	llg m = 0,tmp = n;
	while(tmp)
	{
		m = (tmp%10)+m*10;
		tmp = tmp/10;
	}
	if(m == n)	return 1;
	else		return 0;
}
int bin(llg x,llg y)
{
	int i,j;
	p[40] = 100000000000001ll;
	for(i = 0;i<41;i++)
	{	
		if(p[i] >= x)	break;
	}
	for(j = 0;j<41;j++)
	  if(p[j] >= y) break;

	if(x == y && p[i]==x) return 1;
	else if(x == y && p[i]!=x) return 0;

	if(p[i]==x && p[j]==y)	return j-i+1;
	else if(p[i] == x && p[j]!=y)	return j-i;
	else if(p[i] != x && p[j]==y)	return j-i+1;
	else if(x>4004009004004ll && y>4004009004004ll)	return 0;
	else if(x>4004009004004ll || y>4004009004004ll)	return j-i-1;
	else					return j-i;
}
int main()
{
	freopen("C-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);
	llg i,j,k;
//	p[pn++] = 1;p[pn++] = 4;p[pn++] = 9;
	p[pn++] = 1;
	memset(vis,0,sizeof(vis));
	for(i = 2;i<=10000000;i++)
	{
		j = sqrt(i);
	//	printf("j = %lld i = %lld %d\n",j,i,pali(i));
		vis[i] = pali(i);
		if(vis[j] == 1 && vis[i] == 1 && j*j == i)
		{
			p[pn++] = i;		
		}
		if(vis[i] == 1)
		{
			llg tmp = i*i;
			if(pali(tmp))
			{
				if(tmp>=10000000)
				{
					pp[ppn++] = tmp;
				}
			}
		}
	}
	for(i = 0;i<ppn;i++)
	{
		p[pn] = pp[i]; 
		pn++;
	}
/*	for(i = 0;i<=50;i++)
	{
		j = sqrt(p[i]);
		printf("%lld %lld\n",j,p[i]);
	}*/
	llg x,y;
	int t;
	cin>>t;
	int count = 0;
	while(t--)
	{
		cin>>x>>y;
		count++;
		cout<<"Case #"<<count<<": "<<bin(x,y)<<endl;
	}	
	return 0;
}
