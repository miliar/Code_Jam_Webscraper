#include<stdio.h>
#include<string.h>
#include<iostream>

using namespace std;
char pie[100];

int findlast()
{
	int length = strlen(pie);
	int j;
	for(j=length-1;pie[j]!='-';j--)
		if(j==0) return -1;
	return j;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		if(i>0)	printf("\n");
		scanf("%s",pie);
		int last,trans;	char cur;
		last = findlast();
		trans = (last==-1)?-1:0;
		cur = pie[0];
		for(int j=0;j<=last;j++)
			if(cur!=pie[j])
			{
				trans++;
				cur = pie[j];
			}
		printf("Case #%d: %d",i+1,trans+1);
	}
 } 
