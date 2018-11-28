/*
author:arushi
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,k,c,s,x=0;
	scanf("%d",&t);
	while(t--)
	{
		x++;
		scanf("%d %d %d",&k,&c,&s);
		cout<<"Case #"<<x<<": ";
		for(int i=1;i<=k;i++)
			printf("%d ",i);
		printf("\n");
	}
	return 0;
}