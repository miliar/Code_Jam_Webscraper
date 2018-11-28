/*
Author :codelord
problem :
contest :GCJ R1b=
*/

#include<string.h>
#include<math.h>
#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{	int t;
	int l;
	int a,b,n,x;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%d %d %d",&a,&b,&n);
		int counter =0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{	x = i&j;
				if(x<n&&x>=0)
					counter++;
			}
		}
		printf("Case #%d: %d\n",k,counter);
		
	}
	
}
