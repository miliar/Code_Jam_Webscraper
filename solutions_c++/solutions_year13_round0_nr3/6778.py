#include<stdio.h>
#define max 1005

int v[]={1,4,9,121,484};

int hash[max],ctr[max];

int main()
{
	freopen("c.in","r",stdin);
	freopen("outputc.txt","w",stdout);
	int t,a,b,i,j=1;
	for(i=0;i<5;i++)
	{
		hash[v[i]]=1;
	}
	ctr[0]=0;
	for(i=1;i<max;i++)
	{ctr[i]=ctr[i-1]+hash[i];
	}
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&a,&b);
		printf("Case #%d: %d\n",j++,ctr[b]-ctr[a-1]);
		
	}
return 0;}
