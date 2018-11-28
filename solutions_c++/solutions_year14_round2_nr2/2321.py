#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,n,i,j,k,p,m;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{	
		int c=0;
		scanf("%d%d%d",&n,&m,&p);
		for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		if((i&j)<p)
		c++;
		printf("Case #%d: %d\n",k,c);
	}
	return 0;
}
