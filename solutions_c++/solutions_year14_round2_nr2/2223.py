#include<iostream>
#include<string>
#include<cmath>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{freopen("B-small-attempt0 (2).in","r",stdin);
freopen("out.txt","w",stdout);
int test,x,y,z,p;
scanf("%d",&test);
for(p=1;p<=test;p++)
{
	scanf("%d",&x);
	scanf("%d",&y);
	scanf("%d",&z);
	long long int i,j,total=0;
	long long int m=max(x,y);
	long long int n=min(x,y);
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if((i&j)<z)
			total++;
		}
	}
	printf("Case #%d: %d\n",p,total);
		  }
return 0;
}
