#include <iostream>
#include <cstdio>
using namespace std;

int c[20];

int main() 
{
	int i,j,k,t,r1,r2,n,co;
	scanf("%d",&t);
	co=0;
	while(t--)
	{
		++co;
		for(i=1;i<=16;++i) c[i]=0;
		scanf("%d",&r1);
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				scanf("%d",&k);
				if(i==r1-1)
				{
					++c[k];
				}
			}
		}
		scanf("%d",&r2);
		n=0;
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				scanf("%d",&k);
				if(i==r2-1)
				{
					if(c[k]==1)
					{
	
						if(n==0) n=k;
						else 
						{
							n=-1;
						}
					}
				}
			}
		}
		if(n==0)
		{
			printf("Case #%d: Volunteer cheated!\n",co);
		}
		else if(n==-1)
		{
			printf("Case #%d: Bad magician!\n",co);
		}
		else if(n>0)
		{
			printf("Case #%d: %d\n",co,n);
		}
	}
	return 0;
}