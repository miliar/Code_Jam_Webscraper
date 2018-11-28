#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

int k,c,s,t;

int main()
{
	freopen("g4.in","r",stdin);
	freopen("g4.out","w",stdout);
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii++)
	{
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",ii);
		for(int i = 1; i <= k; i++)
			printf(" %d",i);
		printf("\n");
	}
	return 0;
}
