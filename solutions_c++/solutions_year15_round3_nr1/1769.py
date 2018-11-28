#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int binary(int r,int c,int w)
{
	if(w==c)
		return c;
	else
	{
		return (ceil((c*1.0)/w)-1 + w);
	}
}
int main()
{
	int t,i,result,r,c,w;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d %d",&r,&c,&w);
		result =binary(r,c,w);
			printf("Case #%d: %d\n",i,result);
	}
	return 0;
}
