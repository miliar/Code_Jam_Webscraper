#include<bits/stdc++.h>
using namespace std;
int arr[1005][1005];
void precomp()
{
	int i,j;
	for(i=0;i<=1000;i++)
	for(j=0;j<=1000;j++)
		arr[i][j] = (i&j);	
}
int main()
{
	int tt,t,i,j,a,b,k;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%d%d%d",&a,&b,&k);
		int res=0;
		for(i=0;i<a;i++)
		for(j=0;j<b;j++)
			if((i&j)<k)res++;
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;	
}
