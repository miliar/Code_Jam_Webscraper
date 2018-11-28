#include <iostream>
#include <cstdio>
using namespace std;

int T;
int X, Y;
int a[101][101];

int main(void)
{
	int i,j,k,l;
	scanf(" %d",&T);
	for(i=1;i<=T;i++)
	{
		scanf(" %d %d",&X,&Y);
		for(j=0;j<X;j++)
		{
			for(k=0;k<Y;k++)
			{
				scanf(" %d",&a[j][k]);
			}
		}
		
		
		for(j=0;j<X;j++)
		{
			for(k=0;k<Y;k++)
			{
				
				bool passed = true;
				for(l=0;l<X;l++)
				{
					if(a[l][k] > a[j][k])
					{
						passed = false;
					}
				}
				
				if(passed) continue;
				
				for(l=0;l<Y;l++)
				{
					if(a[j][l] > a[j][k])
					{
						goto here;
					}
				}
			}
		}
		printf("Case #%d: YES\n",i);
		continue;
		here:;
		printf("Case #%d: NO\n",i);
	}
	
	return 0;
}
