#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;
int t,n,input,jum[2510];
vector <int> temp;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		temp.clear();
		memset(jum,0,sizeof(jum));
		scanf("%d",&n);
		for(int j=0;j<(2*n-1)*n;j++)
		{
			scanf("%d",&input);
			jum[input]++;
		}
		for(int j=1;j<=2500;j++)
		{
			if(jum[j]%2==1)
			temp.push_back(j);
		}
		printf("Case #%d: ",i);
		for(int j=0;j<temp.size();j++)
		{
			printf("%d",temp[j]);
			if(j!=temp.size()-1)
			printf(" ");
		}
		printf("\n");
	}
}
