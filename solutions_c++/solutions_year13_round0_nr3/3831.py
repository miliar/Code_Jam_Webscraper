#include<stdio.h>
#include<string.h>
#define MAXN 1000
int fair[MAXN+3];

bool pal(int x)
{
	char c[100];
	sprintf(c,"%d",x);
	int l=strlen(c)-1;
	for(int i=0;i<l;i++,l--)
	{
		if(c[i]!=c[l])	return false;
	}
	return true;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=MAXN;i++)
	{
		if(pal(i))
		{
			int k=i*i;
			if(pal(k)&&k<MAXN)
				fair[k]=1;
		}
		//printf("%7d %7d\n",i,fair[i]);
	}
	int a,b;
	for(int cs=1;cs<=T;cs++)
	{
		scanf("%d%d",&a,&b);
		int cont=0;
		for(;a<=b;a++)
		{
			if(fair[a])
				cont++;
		}
		printf("Case #%d: %d\n",cs,cont);
	}
	return 0;
}
