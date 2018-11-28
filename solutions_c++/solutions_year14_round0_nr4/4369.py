#include <cstdio>
#include <algorithm>

using namespace std; 

int cases, blocks, war, decep, minb; 
double ken[1005], naomi[1005];
int kvalid[1005], nvalid[1005];

int main()
{
	scanf("%d", &cases);
	for(int q=1; q<=cases; q++)
	{
		war=0;
		decep=0;
		scanf("%d", &blocks);
		for(int i=1; i<=blocks; i++)
			scanf("%lf", &naomi[i]), nvalid[i]=1;
		for(int i=1; i<=blocks; i++)
			scanf("%lf", &ken[i]), kvalid[i]=1;
		sort(naomi+1, naomi+1+blocks);
		sort(ken+1, ken+1+blocks);
		for(int i=1, j; i<=blocks; i++)
		{
			for(j=1; j<=blocks; j++)
			{
				if(kvalid[j] && ken[j]>naomi[i])
					break;
			}
			if(j<=blocks)
				kvalid[j]=0;
			else
				war++;
			
		} 
		for(int i=1, j=1; i<=blocks; i++)
		{
			if(naomi[i]>ken[j])
				decep++, j++;
		} 
		printf("Case #%d: %d %d\n", q, decep, war); 
	}
}
