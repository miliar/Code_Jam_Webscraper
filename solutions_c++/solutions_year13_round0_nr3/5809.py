#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int pal[1005];
int sq[1005];
int ps[1005];
int palin(int n)
{
	if(n<10)return 1;
	else if(n<100)
	{
		if(n%10==n/10)return 1;
		else return 0;
	}
	else
	{
		if(n%10==n/100)return 1;
		else return 0;
	}
}

int main()
{
	memset(pal,0,sizeof(pal));
	memset(sq,0,sizeof(sq));
	memset(ps,0,sizeof(ps));
	for(int i=1;i<=1000;i++)
	{
		if(palin(i))
		{
		//	printf("%d\n",i);
			pal[i]=1;
			if(i*i<1000)sq[i*i]=1;
		}
		
	}
	int jum = 0;
	for(int i=1;i<=1000;i++)
	{
		if(pal[i]==1&&sq[i]==1)
		{
		//	printf("%d\n",i);
			jum++;
		}
		ps[i]=jum;
	}
	int t;
	scanf("%d",&t);
	for(int it=0;it<t;it++)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		printf("Case #%d: %d\n",it+1,ps[b]-ps[a-1]);
	}
	return 0;
}
